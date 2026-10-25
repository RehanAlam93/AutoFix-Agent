"""This module handles the core integration with Google's Gemini API to analyze
source code, detect bugs, security flaws, and generate production-ready refactored code."""


import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from the local .env file
load_dotenv()

# Retrieve and configure the Gemini API key securely from environment variables
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
  genai.configure(api_key=api_key)


def analyze_and_refactor_code(source_code: str) -> dict:
  """Analyze the provided source code using Gemini LLM to detect bugs,

  security vulnerabilities, and provide a production-ready refactored version.

  Args:
      source_code (str): The raw source code string submitted by the user.

  Returns:
      dict: A dictionary containing either the AI analysis result text or an error message.
  """
  # Validate that the API key is present before attempting to call the Gemini service
  if not api_key:
    return {
        "error": "Gemini API key is missing. Please check your .env file."
    }

  try:
    # Initialize the GenerativeModel instance with the recommended model version
    model = genai.GenerativeModel("gemini-3.8-flash")

    # Construct a structured prompt enforcing a strict response format for code evaluation
    prompt = f"""
        You are an expert Senior Software Engineer and Code Reviewer.
        Analyze the following source code for logical bugs, security vulnerabilities, performance issues, and anti-patterns.

        Provide your response strictly in the following format:

        ### ISSUES FOUND:
        - [List each bug, security flaw, or bad practice found, with a brief explanation]

        ### REFACTORED CODE:
        [Provide the fully corrected, clean, and production-ready code inside a markdown code block]

        Here is the source code to review:
        {source_code}
        """

    # Generate content using the Gemini model API
    response = model.generate_content(prompt)

    # Return the successful response payload containing the AI feedback
    return {"analysis_result": response.text}

  except Exception as e:
    # Handle runtime or network exceptions gracefully and return a structured error response
    return {"error": f"Failed to generate analysis from AI model: {str(e)}"}