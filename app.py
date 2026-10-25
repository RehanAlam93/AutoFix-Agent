"""Module: Flask Web Application & Routing

This module handles web requests, validates syntax, triggers AI code analysis,
and automatically saves the generated refactored output into a local 'fixed_codes' folder.
"""

from datetime import datetime
import os
from flask import Flask, jsonify, render_template, request
from agent.analyzer import analyze_and_refactor_code
from agent.validator import validate_python_code

# Initialize Flask application
app = Flask(__name__)

# Define the folder where fixed outputs will be saved automatically
OUTPUT_DIR = "fixed_codes"
os.makedirs(OUTPUT_DIR, exist_ok=True)


@app.route("/")
def index() -> str:
  """Render the main frontend HTML webpage."""
  return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze() -> tuple:
  """Handle code submission, validate, analyze via AI, and save the output to a local folder."""
  data = request.json
  source_code = data.get("code", "")

  # Validate that the code input is not empty
  if not source_code.strip():
    return jsonify({"error": "Code input cannot be empty."}), 400

  # Step 1: Validate Python code syntax using AST validator
  is_valid, syntax_error = validate_python_code(source_code)

  # Step 2: Send source code to Gemini AI analyzer
  ai_response = analyze_and_refactor_code(source_code)

  if "error" in ai_response:
    return jsonify({"error": ai_response["error"]}), 500

  analysis_result = ai_response["analysis_result"]

  # Step 3: Automatically save the AI analysis result into the 'fixed_codes' folder
  try:
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    file_path = os.path.join(OUTPUT_DIR, f"fixed_code_{timestamp}.txt")

    with open(file_path, "w", encoding="utf-8") as f:
      f.write(
          f"--- INPUT CODE ---\n{source_code}\n\n--- AI ANALYSIS & REFACTORED"
          f" CODE ---\n{analysis_result}"
      )
  except Exception as e:
    print(f"Warning: Failed to save output to file: {e}")

  # Return JSON response to the frontend UI
  return jsonify({
      "success": True,
      "syntax_valid": is_valid,
      "syntax_error": syntax_error,
      "analysis": analysis_result,
  })


if __name__ == "__main__":
  app.run(debug=True)