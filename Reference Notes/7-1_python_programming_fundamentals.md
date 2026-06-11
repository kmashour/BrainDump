---
domains:
  - "python"
---

# Module 7-1: Python Programming Fundamentals

This module covers core Python programming constructs, virtual environments management using Pyenv, and developing web applications using the Flask framework.

---

## 1. Pyenv and Virtual Environments

Managing multiple Python environments requires separating system binaries from project dependencies.
*   **Pyenv:** Manages system-level installation of different Python versions (e.g., `pyenv install 3.11.0`).
*   **Venv:** Creates an isolated virtual environment directory containing a private copy of python binaries and libraries:
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate
    ```

---

## 2. Flask Web Framework Fundamentals

Flask is a WSGI micro-web framework designed for simple routing and API development.

#### Deep-Intuition (AARF) Breakdown:
1. **The Answer (Core Pattern):** Declare a clean entrypoint, define path routes, and run using configuration-driven parameters:
    ```python
    from flask import Flask, jsonify
    app = Flask(__name__)

    @app.route("/api/health", methods=["GET"])
    def health_check():
        return jsonify({"status": "healthy"}), 200

    if __name__ == "__main__":
        app.run(host="0.0.0.0", port=5000)
    ```
2. **The Assumptions (Context):** Project dependencies must be logged in a `requirements.txt` file and installed inside the activated virtual environment.
3. **The Rationale (Why):** Minimal design allows developers to import only the packages they need, preventing framework overhead and boilerplate code.
4. **The Failure Loop (What if not):** Running Flask using global system Python packages (`sudo pip install`) pollutes the system operating system libraries. OS updates can break python packages, causing application compilation failure.
5. **Alternative Case (When to use 'if not'):** For complex, large-scale enterprise APIs requiring automated database migration tooling out-of-the-box, utilize Django instead of Flask.
