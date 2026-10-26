
# Environment Configuration
#
# Loads PostgreSQL connection settings from a local .env
# file so credentials are not stored directly in source
# code or committed to GitHub.
# =========================================================

import os
from dotenv import load_dotenv

# Load environmental variables from the .env file.
load_dotenv()

# Database connection settings.
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")