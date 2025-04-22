#!/usr/bin/env python3
"""
Crucible API - Entry point for the Flask application
"""
from crucible import create_app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)