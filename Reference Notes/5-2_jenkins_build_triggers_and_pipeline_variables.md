---
domains:
  - "jenkins"
---

# Module 5-2: Jenkins Build Triggers & Variables

This module details mechanisms for triggering Jenkins pipelines (Webhooks, Poll SCM, Cron) and managing pipeline variables (static environments, dynamic scripted environments, parameters) along with integrating JUnit test reporting.

---

## 1. Pipeline Variables: Static environment {} vs. Dynamic script {} Scoping

Jenkins pipelines leverage environment variables to parameterize builds. However, Declarative Pipeline compile-time structures differ significantly from Groovy script runtimes.

### 🔄 Comparison of Variable Scopes

| Feature | Static `environment {}` Block | Dynamic `env.MYVAR` inside `script {}` |
| :--- | :--- | :--- |
| **Evaluation Timing** | Before the pipeline starts (during syntax parsing). | At runtime (when the specific step executes). |
| **Logic & Functions** | ❌ Forbidden. Syntax checks will reject function calls. | ✅ Supported. Can call standard Groovy/Java methods. |
| **Shell Command Capture** | ❌ Forbidden. Cannot use `sh(..., returnStdout: true)`. | ✅ Supported. Capture utility CLI stdout strings. |
| **Credential Binding** | ✅ Supported natively via the `credentials()` helper. | ✅ Supported via `withCredentials` block helpers. |
| **Scope** | Globally or local to the declared `stage`. | Global across downstream steps after assignment. |

### 🛠️ Static and Dynamic Variable Implementations

#### Deep-Intuition (AARF) Breakdown:
1.  **The Answer (Core Config):** Use the static `environment {}` block for compile-time configurations, and a setup `script {}` block to dynamically capture runtime values:
    ```groovy
    // Global variable declaration for dynamic scoping
    def dynamicCommitHash = ""

    pipeline {
        agent any
        environment {
            APP_NAME    = "microservice-auth"                 // ✅ Static String
            DB_CREDS    = credentials("postgres-user-pass")  // ✅ Credential reference
        }
        stages {
            stage('Initialize Runtime Context') {
                steps {
                    script {
                        // Capture Git commit dynamically at runtime
                        dynamicCommitHash = sh(
                            script: "git rev-parse --short HEAD", 
                            returnStdout: true
                        ).trim()
                        
                        // Set environment variable globally for downstream stages
                        env.GIT_COMMIT_SHORT = dynamicCommitHash
                    }
                }
            }
            stage('Build Artifact') {
                steps {
                    echo "Building ${env.APP_NAME} version ${env.GIT_COMMIT_SHORT}"
                }
            }
        }
    }
    ```
2.  **The Assumptions (Context):** Dynamic assignments must be wrapped in a `script {}` block when using Declarative syntax. String interpolation of environment variables requires double quotes (`"${env.VAR_NAME}"`); single quotes (`'${env.VAR_NAME}'`) treat variables as literal strings.
3.  **The Rationale (Why):** Separating static definitions from dynamic runtime scripting prevents syntax evaluation errors during the pre-build pipeline compilation phase.
4.  **The Failure Loop (What if not):** Attempting to execute commands or define function variables directly within a declarative `environment {}` block causes compilation failures immediately upon checkout:
    ```
    WorkflowScript: 6: Environment variable values must be string literals or credential helper calls.
    ```
5.  **Alternative Case (When to use 'if not'):** If the pipeline only consumes user-supplied parameters, define a static `parameters {}` block (e.g., `booleanParam`, `choice`, `string`) at the root level, bypassing custom script capture blocks.

---

## 2. Pipeline Triggering Configurations: Webhooks, Poll SCM, & Cron

Automating pipeline execution requires matching the trigger strategy to the availability of the network topology and source control server.

### 🗺️ Triggering Strategies Matrix

*   **Webhook Triggers (Push):** The VCS (GitHub/Gitea) pushes an HTTP POST payload to the Jenkins listener `/github-webhook/` immediately when a commit is pushed. This is the gold standard for CI/CD.
*   **Poll SCM (Git Polling):** Jenkins queries the Git repository metadata periodically to detect changes.
*   **Build Periodically (Cron Scheduler):** Runs builds at set times, regardless of code changes.

### ⚙️ Configuring Cron & Git Polling Schedules

#### Deep-Intuition (AARF) Breakdown:
1.  **The Answer (Core Config):** Define SCM polling or cron parameters within the pipeline's `triggers` block. Use the `H` (Hash) parameter to load-balance scheduling:
    ```groovy
    pipeline {
        agent any
        triggers {
            // Option A: Poll SCM every 15 minutes, hash-distributed
            pollSCM('H/15 * * * *')
            
            // Option B: Run nightly regression builds at ~2:30 AM
            cron('H(30-45) 2 * * *')
        }
    }
    ```
2.  **The Assumptions (Context):**
    *   *Poll SCM:* Requires credentials to pull Git repository metadata.
    *   *Webhooks:* Requires the Jenkins controller to be accessible over the public internet or private network paths by the Git provider's webhook dispatchers.
3.  **The Rationale (Why):** The `H` symbol hashes the job name to spread out execution times. For example, if ten jobs are scheduled at `0 0 * * *` (midnight), they all start concurrently, exhausting CPU cores and disk I/O. Using `H 0 * * *` assigns a different minute to each job, smoothing infrastructure resource utilization.
4.  **The Failure Loop (What if not):**
    *   *Polling Rate Limits:* Configuring aggressive polling (`* * * * *` to check every minute) without using webhooks can trigger API rate limits on providers like GitHub, resulting in blocked build executions:
        ```
        Fatal: Git remote polling failed. Status Code 403: API rate limit exceeded.
        ```
    *   *Interval Syntax Gotcha:* Writing `H/1 * * * *` in Jenkins does **not** poll every minute. It resolves to a single hashed minute *within the hour* (e.g., at minute 42, running once per hour). To check every minute, use `* * * * *`.
5.  **Alternative Case (When to use 'if not'):** If the Jenkins server is completely firewalled off from outbound internet access and GitHub webhooks cannot reach it, SCM polling (`H/5 * * * *` or similar interval) acts as the only viable fallback mechanism.

---

## 3. JUnit Test Report Integration

Publishing test reports provides developers with historical data, failure tracking, and test quality trends over time.

### 🧪 Configuring JUnit Assertions & Reports

#### Deep-Intuition (AARF) Breakdown:
1.  **The Answer (Core Config):** Configure test runners to output reports in the standard JUnit XML format, then parse them inside a `post` execution block:
    ```groovy
    pipeline {
        agent { label 'test-runner' }
        stages {
            stage('Execute Tests') {
                steps {
                    // Force zero exit code workaround if testing framework doesn't support failures gracefully
                    sh 'npm run test -- --reporter junit --output test-results/junit.xml'
                }
            }
        }
        post {
            always {
                // Parse test outputs regardless of compile failures
                junit testResults: 'test-results/junit.xml', allowEmptyResults: false
            }
        }
    }
    ```
2.  **The Assumptions (Context):** The JUnit plugin must be active in Jenkins. The target path must match the folder created by the testing framework's reporter.
3.  **The Rationale (Why):** Wrapping `junit` inside the `always {}` post block ensures that test results are parsed and published even when tests fail. If placed in `success {}`, failed tests (which trigger non-zero shell exit codes) skip the reporting phase, hiding critical debug stack traces from the UI.
4.  **The Failure Loop (What if not):** If tests fail and the `junit` step is placed outside an `always` post block, the pipeline aborts immediately, leaving no parsed records. The Jenkins UI will not show the "Test Result Trend" graph, forcing developers to scan raw console text files to find failing assertions.
5.  **Alternative Case (When to use 'if not'):** If the build environment runs in an air-gapped system where XML reports cannot be generated, fall back to archiving the stdout logs using the `archiveArtifacts` step.

---

### CKA / DevOps Tip
> [!TIP]
> After configuring a JUnit step, run the build 2 to 3 times. Jenkins requires multiple builds to generate enough comparative data points to populate the interactive **Test Result Trend** graph on the job control page.
