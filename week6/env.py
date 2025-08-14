"""
This file shows how to load configuration from a .env file and access it via
environment variables in Python.

Flow:
1) load_dotenv() reads key=value pairs from a local .env file and exports them
   to the current process environment.
2) os.getenv("API_KEY") retrieves the value assigned to API_KEY. If the key is
   missing, it returns None instead of crashing the program.

Tips:
- Do not commit your .env file. It is already ignored by .gitignore in this repo.
- After calling load_dotenv(), you can access any variables defined in .env using os.getenv.
"""

import os
from dotenv import load_dotenv

# Load variables from .env into environment
load_dotenv()

# Read your API key (returns None if not present)
api_key = os.getenv("API_KEY")

# Example debug print (optional):
# print("API_KEY present?", bool(api_key))