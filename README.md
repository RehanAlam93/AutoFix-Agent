# 🤖 AutoFix-Agent — AI-Powered Python Code Reviewer & Auto-Fixer

AutoFix-Agent is a lightweight, AI-powered Python code review and refactoring web application built with Flask and Google's Gemini API. It analyzes Python source code to identify potential bugs, security vulnerabilities, performance issues, and bad coding practices, then suggests improved code.

The application combines Python's built-in Abstract Syntax Tree (AST) parser for syntax validation with AI-powered analysis and a responsive web interface.

> **Project Status:** Working prototype / portfolio project. AI-generated code should be reviewed and tested before production use.

## 🌟 Overview

AutoFix-Agent helps developers review Python code more efficiently by combining syntax validation with AI-generated code review and refactoring suggestions.

Users can paste Python code into a web interface, submit it for analysis, review potential issues, and copy the suggested refactored output.

### 🎯 Project Goals
- Automate parts of Python code review.
- Identify syntax errors before returning analysis results.
- Detect potential logical bugs and security vulnerabilities.
- Suggest cleaner and more maintainable code.
- Provide an easy-to-use browser-based interface.
- Avoid application-level database persistence in the current analysis workflow.


### ⚡ AI-Powered Code Review
Uses Google's Gemini API to analyze submitted Python code for:
- Potential logical bugs.
- Security vulnerabilities.
- Performance issues.
- Poor coding practices.
- Unnecessary complexity and anti-patterns.

### 🔍 Python Syntax Validation
- Uses Python's built-in `ast` module to check whether submitted Python code is syntactically valid.
- When a syntax error is detected, the validator reports the line number and error description.
- *Example:* `SyntaxError at line 3: expected ':'`
- AST validation checks syntax, not whether a program is logically correct or secure.

### 🛠️ AI-Based Code Refactoring
The AI is prompted to return its results in two sections:
- **ISSUES FOUND:** Potential bugs, security flaws, and bad practices.
- **REFACTORED CODE:** A proposed improved version of the source code.
The generated code is displayed for the user to review. The application does not automatically execute or write the suggested changes to source files.

### 💻 Web-Based User Interface
The frontend is built with HTML, JavaScript, and Tailwind CSS. Users can:
- Paste Python source code.
- Submit code for analysis.
- View AI-generated review results.
- Check syntax validation status.
- Copy the displayed output to the clipboard.

### 🔌 Flask API
Provides a Flask backend with an `/analyze` endpoint that accepts JSON requests and returns analysis results.

### 🗄️ SQLite Database Helper
The project includes a SQLite module that can create a `code_audits` table for storing source code, detected issues, refactored code, and timestamps.
> *Note: The database helper is not currently integrated into the active `/analyze` route, so analysis results are not saved through the current workflow.*

### 🔐 Environment-Based API Key
Loads the Gemini API key from a local `.env` file using `python-dotenv`, keeping credentials separate from the application source code.

---

## 🔄 How It Works

```text
User submits Python code
          │
          ▼
Flask receives POST /analyze
          │
          ▼
Check for empty input
          │
          ▼
Validate syntax using Python AST
          │
          ▼
Send source code to Gemini API
          │
          ▼
AI identifies issues and suggests fixes
          │
          ▼
Flask returns a JSON response
          │
          ▼
Frontend displays the results
          │
          ▼
User reviews and copies the output


📁 Project Structure

AutoFix-Agent/
├── agent/
│   ├── analyzer.py
│   └── validator.py
├── agent_env/
├── fixed_codes/
│   └── fixed_code_202610...py
├── templates/
│   └── index.html
├── .env
├── .gitignore
├── app.py
├── README.md
└── requirements.txt
