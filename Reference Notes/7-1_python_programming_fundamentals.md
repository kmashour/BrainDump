---
domains:
  - "python"
---

# Module 7-1: Python Programming Fundamentals

This module covers core Python programming concepts, object data formatting, collections utilities, pyenv version management, isolated virtual environments, dependency configuration, styling and unit testing standards, and Flask web application architecture using the App Factory pattern.

---

## 1. Pyenv and Python Version Management

Operating systems often rely on specific system Python interpreter versions. Installing developer packages directly into the system environment can break core OS utilities. `pyenv` resolves this by managing multiple independent system-level installations of different Python versions.

### Core `pyenv` CLI Commands
*   **List Available Versions:** Show all downloadable Python interpreters:
    ```bash
    pyenv install --list
    ```
*   **Install Specific Version:** Download and compile a target version:
    ```bash
    pyenv install 3.11.0
    ```
*   **List Installed Versions:** View all local versions (with active selection indicator):
    ```bash
    pyenv versions
    ```
*   **Check Active Version:** View the version currently running in the shell:
    ```bash
    pyenv version
    ```
*   **Local Directory Scope:** Set a Python version specific to a directory and its subdirectories (writes version to a `.python-version` file):
    ```bash
    pyenv local 3.11.0
    ```
*   **Global System Scope:** Set the fallback Python version for the entire OS user profile:
    ```bash
    pyenv global 3.11.0
    ```

---

## 2. Isolated Virtual Environments & Dependency Management

### Virtual Environment (Venv) Mechanics
Creating a virtual environment replicates Python binaries and pip packages inside a local directory. When activated, the shell's environment variables (specifically `PATH`) are updated. The Python interpreter modifies `sys.path` dynamically, forcing all package imports to search inside the virtual environment's private `site-packages` directory instead of global system paths.

*   **Creation:**
    ```bash
    python3 -m venv .venv
    ```
    *Using Pyenv explicitly to guarantee version:*
    ```bash
    pyenv exec python -m venv .venv
    ```
*   **Activation:**
    *   *Linux/macOS (Bash/Zsh):*
        ```bash
        source .venv/bin/activate
        ```
    *   *Windows (PowerShell):*
        ```powershell
        .\.venv\Scripts\Activate.ps1
        ```

### Dependency Configuration (`requirements.txt`)
Manage project requirements using precise version pinning to ensure identical environments across deployments:
*   `==` : Install exactly this version (strict reproducibility). E.g., `requests==2.31.0`.
*   `>=` : Install the latest version matching or above the defined value. E.g., `flask>=2.0.0`.
*   `,` : Compound range restrictions. E.g., `flask>=1.1.2,<2.0` (allows patch/minor upgrades, blocks breaking major upgrades).
*   `[...]` : Specify optional extra dependencies. E.g., `pymongo[srv]==3.11` (installs pymongo alongside DNS SRV dependencies).

```bash
# Install dependencies from configuration
pip install -r requirements.txt
```

#### Deep-Intuition (AARF) Breakdown: Virtual Environments
1.  **The Answer (Core Pattern):** Build isolated dependency trees per project and restrict global scopes:
    ```bash
    pyenv local 3.10.7
    pyenv exec python -m venv .venv
    source .venv/bin/activate
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
2.  **The Assumptions (Context):** Assumes the target directory has run `pyenv local` and packages are installed inside the activated shell environment.
3.  **The Rationale (Why):** Separating dependencies prevents library version conflicts (e.g., App A needing Django 3, App B needing Django 5) and isolates OS package managers from developer scripts.
4.  **The Failure Loop (What if not):** Running packages in the global environment (`sudo pip install`) overwrites system packages. Subsequent system updates can break dependencies, causing immediate runtime crashes or host boot issues.
5.  **Alternative Case (When to use 'if not'):** In containerized environments (Docker), virtual environments are optional. Since the container itself provides complete OS isolation, global installations are safe.

---

## 3. Data Structures, Formatting & Flow Statements

### Float Formatting & Precision
Format float output to restrict decimal representation and align character widths:
```python
num = 23.45678

# Using format() method (width: 10, precision: 4 decimal places, float representation)
print("My 10 character, four decimal number is:{0:10.4f}".format(num))

# Using modern f-strings (equivalent layout)
print(f"My 10 character, four decimal number is:{num:10.4f}")
```
*Output:*
```
My 10 character, four decimal number is:   23.4568
```

### Enumeration & List Unpacking
`enumerate()` returns an iterator of index-value tuples from a sequence, allowing clean unpacking:
```python
word = "abcd"
for index, letter in enumerate(word):
    print(f"Index: {index}, Letter: {letter}")
```

### List Zipping
`zip()` merges multiple iterables into an iterator of tuples, stopping at the shortest input list:
```python
list1 = ["a", "b", "c", "d"]
numbers = [1, 2, 3, 4, 5, 6]
zipped = list(zip(list1, numbers))
# Result: [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
```

### Generator Expressions with `all()` and `any()`
Using standard list comprehensions to check conditions creates a full list in memory. Combining generator expressions with built-in boolean validators performs lazy evaluation, halting execution as soon as the result is determined:
```python
numbers = [2, 4, 6, 8]

# Check if ALL items are even (returns True on first mismatch if false)
all_even = all(num % 2 == 0 for num in numbers)  # True

# Check if ANY item is odd
any_odd = any(num % 2 != 0 for num in numbers)   # False
```

### Random Module Utilities
*   `random.shuffle(lst)`: Modifies a list in-place, shuffling the sequence order randomly.
*   `random.randint(a, b)`: Returns a random integer $N$ such that $a \le N \le b$ (both endpoints inclusive).

---

## 4. Linting, Styling, & Unit Testing Standards

Maintaining codebases requires code styling checkers and regression testing tools:

### Linting & Style Enforcement
*   **Pylint:** Scans Python files for syntax compliance, coding standards violations, and potential bugs.
*   **Pyflakes:** Performs rapid static analysis to identify logical bugs (like unused imports or undefined variables) without executing the code.
*   **PEP8:** Checks compliance with the official Python style guide guidelines (spacing, variable naming, line length limits).

### Verification & Testing
*   **unittest:** Standard library testing framework supporting test fixtures, test cases, and test suites.
*   **doctest:** Searches code docstrings for text that looks like interactive Python sessions, executing those sessions to verify the code behaves exactly as documented.

---

## 5. Flask Web Framework & App Factory Pattern

Flask is a lightweight WSGI micro-web framework. While basic scripts configure routes globally on a single `app` instance, production setups use the **App Factory Pattern** to instantiate the app context inside a lifecycle function.

#### Deep-Intuition (AARF) Breakdown: Flask App Factory Pattern
1.  **The Answer (Core Pattern):** Wrap application initialization inside a `create_app()` function, configuring dependencies, blue-prints, and database clients locally on the app context:
    ```python
    import datetime
    from flask import Flask, render_template, request, jsonify
    from pymongo import MongoClient

    def create_app(config_class=None):
        app = Flask(__name__)
        
        # Initialize database pool bound to application instance
        client = MongoClient("mongodb+srv://user:password@cluster.mongodb.net/")
        app.db = client.microblog

        @app.route("/", methods=["GET", "POST"])
        def home():
            if request.method == "POST":
                entry_content = request.form.get("content")
                formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")
                
                # Insert document into MongoDB collection
                app.db.entries.insert_one({"content": entry_content, "date": formatted_date})

            # Fetch all entries (no filters) and format dates
            entries_with_date = [
                (
                    entry["content"],
                    entry["date"],
                    datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d")
                )
                for entry in app.db.entries.find()
            ]
            return render_template("home.html", entries=entries_with_date)

        @app.route("/api/health", methods=["GET"])
        def health():
            return jsonify({"status": "healthy"}), 200

        return app

    if __name__ == "__main__":
        app = create_app()
        app.run(host="0.0.0.0", port=5000)
    ```
2.  **The Assumptions (Context):** Environment variables must point to the factory script. E.g., `export FLASK_APP="app:create_app()"` and dependencies (such as `pymongo` and `dnspython`) must be installed.
3.  **The Rationale (Why):** Declaring the database connection pool inside a factory function guarantees that connections are isolated per application context. It allows testing suites to boot the app dynamically with mocked databases or specific config parameters without modifying the source code.
4.  **The Failure Loop (What if not):** Initializing connections globally (outside functions) creates active sockets during file compilation. If the web server runs multiple WSGI worker processes (e.g., Gunicorn), the processes inherit open connections, causing connection pool exhaustion, file descriptor leaks, and database locks.
5.  **Alternative Case (When to use 'if not'):** For lightweight, single-file serverless scripts (AWS Lambda functions), define database connections globally to cache and reuse the connection socket across warm container invokes.

---

## 📖 Sources and References
*   Udemy Course: *The Web Developer Bootcamp (Flask & Python)*
