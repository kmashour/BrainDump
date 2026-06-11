Great observation — you're absolutely right to ask this, because it touches on a key subtlety in Jenkins Pipeline design.

### 🚫 Short Answer:

**No**, the `environment {}` block in Declarative syntax **cannot** dynamically assign values or use function calls.  
It **must** use **static strings or credentials** — evaluated **before runtime**.

---

### 🔍 Let's break it down:

#### ❌ `environment {}` limitations:

1. **Cannot use dynamic logic or functions**
    
    ```groovy
    def getEnvValue() {
        return "dynamicValue"
    }
    
    pipeline {
        agent any
        environment {
            MYVAR = getEnvValue()   // ❌ This will fail: not allowed
        }
    }
    ```
    
    - ❌ Jenkins will throw a validation error during compilation.
        
    - ✅ You **can** do this inside a `script {}` block using `env.MYVAR = getEnvValue()`
        
2. **Cannot use shell command output**
    
    ```groovy
    environment {
        MYVAR = sh(script: "date", returnStdout: true)  // ❌ Not allowed
    }
    ```
    
3. **Only allows literal strings or credential references**
    
    ```groovy
    environment {
        MYVAR = "static-value"                  // ✅ Allowed
        SECRET = credentials("my-secret-id")   // ✅ Allowed
    }
    ```
    

---

### ✅ Inside `script {}`, you can do:

```groovy
script {
    def dynamic = "value-${new Date().format('yyyyMMdd')}"
    env.MYVAR = dynamic
}
```

Or:

```groovy
script {
    def output = sh(script: "echo hi", returnStdout: true).trim()
    env.MYVAR = output
}
```

---

### 🔄 Summary Table

|Feature|`environment {}`|`env.MYVAR =` inside `script {}`|
|---|---|---|
|Static string assignment|✅ Yes|✅ Yes|
|Function call|❌ Not allowed|✅ Allowed|
|Shell command output|❌ Not allowed|✅ Allowed|
|Can be used globally/stage-level|✅ Yes|✅ Yes (with logic)|
|Evaluated before pipeline runtime|✅ Yes|❌ No — evaluated at runtime|

---

### 💡 Tip:

If you want to **simulate dynamic environment values globally**, you can do something like this early in the pipeline:

```groovy
def dynamicValue

pipeline {
    agent any

    stages {
        stage('Setup') {
            steps {
                script {
                    dynamicValue = sh(script: 'echo hello', returnStdout: true).trim()
                    env.MYVAR = dynamicValue
                }
            }
        }
        stage('Use it') {
            steps {
                echo "MYVAR is ${env.MYVAR}"
            }
        }
    }
}
```

Let me know if you'd like a reusable pattern or function to assign multiple dynamic env vars in Declarative Pipelines!