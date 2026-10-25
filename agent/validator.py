"""This module provides utility functions to validate raw Python source code strings
for syntax correctness using Python's built-in Abstract Syntax Tree (AST) parser."""

import ast

def validate_python_code(code_string: str) -> tuple[bool, str | None]:
  """Validate whether the given code string has valid Python syntax.

  Args:
      code_string (str): The raw source code string to validate.

  Returns:
      tuple[bool, str | None]: A tuple where the first element is a boolean
        indicating validity, and the second element is the detailed error
        message string if a SyntaxError occurs, or None if valid.
  """
  try:
    # Attempt to parse the source code string into an Abstract Syntax Tree (AST)
    ast.parse(code_string)
    return True, None

  except SyntaxError as e:
    # Extract detailed syntax error metadata (line number and error description) if parsing fails
    error_message = f"SyntaxError at line {e.lineno}: {e.msg}"
    return False, error_message