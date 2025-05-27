# api/index.py
import sys
import os

        # Add the parent directory to the system path so Flask can find your app.py
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

        # Import your Flask app instance
from app import app

        # This is the entry point for Vercel
        # Vercel expects a callable named 'app'
        # Your Flask app instance is already named 'app'
        # So, we just need to make sure it's imported correctly.
