---
domains:
  - "git"
  - "devops"
---

# Git Version Control Fundamentals & Workflows

This module covers Git version control workflows, staging area mechanics, branch management, merge conflict resolution, stashing, and repository rollbacks.

---

## 1. Initializing & Configuring a Repository

Git tracks project files within a local directory by initializing a hidden `.git` database.
*   **Initialization:**
    ```bash
    git init
    ```
*   **Cloning Remote Repositories:** Download an existing repository:
    ```bash
    # Clone into a specific folder name
    git clone https://github.com/username/repo.git target_folder
    
    # Clone into the current directory
    git clone https://github.com/username/repo.git
    ```

---

## 2. Staging Area Mechanics & Working Directories

Git manages code changes across three primary states: the Working Directory (local files), the Staging Area (index of changes to commit), and the Local Repository (committed history database).

### Staging Changes
Add files to the staging index prior to committing:
```bash
# Stage all changes in the current directory
git add .

# Stage a specific file
git add path/to/file.py
```

### Checking Repository Status
```bash
git status
```
*Sample Output:*
```
On branch master
Changes to be committed:
  (use "git reset HEAD <file>..." to unstage)

        modified:   app.py
        modified:   models/user.py
```

### Unstaging Files
To remove a file from the Staging Area while keeping your local modifications untouched in the Working Directory:
```bash
git reset HEAD models/user.py
```

### Discarding Working Directory Changes
To completely revert uncommitted modifications in the Working Directory back to the last commit:
```bash
git checkout -- models/user.py
```
*Note:* The `--` parameter is a delimiter indicating that the subsequent argument `models/user.py` must be interpreted strictly as a file path rather than a branch name or command option, preventing accidental branch switches.

---

## 3. Undoing Local Commits

When rolling back mistakes in local commits, choose the correct undo strategy to prevent history corruption:

#### Deep-Intuition (AARF) Breakdown: Git Revert vs. Git Reset
1.  **The Answer (Core Pattern):**
    *   *Safe Undo (Revert):* Create a new commit that applies inverse changes:
        ```bash
        git log --oneline
        # Identify target hash e.g., ae77aedd
        git revert ae77aedd
        ```
    *   *Destructive Undo (Reset):* Move the branch ref pointer backward, discarding commits:
        ```bash
        git reset --hard ae77aedd
        ```
2.  **The Assumptions (Context):** `git reset` must **never** be used on commits that have already been pushed to shared remote repositories.
3.  **The Rationale (Why):** `git revert` is a non-destructive operation. It preserves the commit history and appends a new commit containing the inverse changes. This ensures that other developers sharing the repository do not experience history mismatches. `git reset` deletes commits from history, rewinding the HEAD pointer.
4.  **The Failure Loop (What if not):** Running `git reset --hard` on pushed commits forces a history mismatch. When pushing, Git will reject the update unless forced (`--force`). If forced, it breaks other team members' local working trees, leading to merge conflicts and lost code.
5.  **Alternative Case (When to use 'if not'):** If commits contain sensitive data (like hardcoded keys) that must be completely purged from the repository history before it becomes public, use `git reset` (or tools like `git-filter-repo`), assuming you coordinate with the team first.

---

## 4. Remote Repository Integration

Connect local git repositories to remote servers (e.g. GitHub, GitLab, Gitea) to share code:
*   **Link Remote URL:** Set the remote target under the alias `origin`:
    ```bash
    git remote add origin https://github.com/username/repo.git
    ```
*   **Push Changes:** Upload local commits and set upstream tracking:
    ```bash
    git push -u origin main
    ```
*   **Pull Changes:** Retrieve and merge updates from the remote repository:
    ```bash
    git pull
    ```

---

## 5. Branch Management & Pointer Labels

Branches are lightweight pointers to specific commits. The special label `HEAD` is a reference pointer tracking the commit you are currently working on in the shell.

*   **List Branches:**
    ```bash
    git branch
    ```
*   **Create a Branch:**
    ```bash
    git branch feature/new-design
    ```
*   **Create and Switch to Branch (Recommended Modern CLI):**
    ```bash
    git switch -c feature/new-design
    ```
*   **Legacy Checkout Switch:**
    ```bash
    git checkout -b feature/new-design
    ```
*   **Switching Branches:**
    ```bash
    git switch feature/new-design
    # or
    git checkout feature/feature-name
    ```

---

## 6. Merging & Conflict Resolution

### Merging Branches
To combine commits from a feature branch into the integration branch (e.g., `master`/`main`):
```bash
git checkout master
git merge feature/new-design
```

### Merge Conflicts
If two developers edit the same lines of the same file concurrently, Git cannot determine which version to keep. The merge pauses, and Git inserts conflict markers:
```
<<<<<<< HEAD
print("Master branch change")
=======
print("Feature branch change")
>>>>>>> feature/new-design
```
*Resolution:* Open the conflicting file, choose the correct code blocks, remove the conflict markers (`<<<<<<<`, `=======`, `>>>>>>>`), stage the resolved files via `git add`, and finalize the merge commit via `git commit`.

---

## 7. Stashing Working Progress

When you need to switch tasks (e.g., pull urgent remote fixes) but your current work is incomplete or in a non-compiling state, use Git Stashing to save changes temporarily.

#### Deep-Intuition (AARF) Breakdown: Git Stash
1.  **The Answer (Core Pattern):** Stash dirty working changes, perform target tasks, and restore the stash:
    ```bash
    # Save local modifications to the stash stack
    git stash
    
    # Verify working directory is clean
    git status
    
    # Perform urgent tasks (e.g., pull updates)
    git pull origin main
    
    # Re-apply the stashed changes
    git stash apply
    ```
2.  **The Assumptions (Context):** Untracked files (newly created files not yet added to Git) are not stashed unless explicitly requested using `git stash -u`.
3.  **The Rationale (Why):** Stashing provides a clean working environment without forcing developers to create dummy "in-progress" commits that pollute the repository history.
4.  **The Failure Loop (What if not):** Attempting to switch branches or pull remote updates while having modified files that conflict with incoming changes causes Git to block the operation. Developers are forced to either discard their work or commit incomplete, broken code.
5.  **Alternative Case (When to use 'if not'):** If the temporary changes represent a logical feature that you plan to develop independently, create a temporary branch and commit the work instead of using the stash stack.

---

## 📖 Sources and References
*   Git Workshop Documentation: [What is a Commit](https://git-workshop.tecladocode.com/docs/what_is_a_commit)
*   Git Stashing Reference: [Git Tools - Stashing and Cleaning](https://git-scm.com/book/en/v2/Git-Tools-Stashing-and-Cleaning)
*   Collaborative workflows: [Working with GitHub](https://git-workshop.tecladocode.com/docs/working_with_github)
