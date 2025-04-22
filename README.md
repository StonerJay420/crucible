# Crucible API

A Flask-based RESTful API application.

## Project Structure

```
crucible/
├── app.py              # Application entry point
├── config.py           # Configuration settings
├── requirements.txt    # Project dependencies
├── .gitignore          # Git ignore file
├── README.md           # Project documentation
├── tests/              # Test directory
└── crucible/           # Application package
    ├── routes/         # Route definitions
    ├── models/         # Data models
    ├── services/       # Business logic
    ├── static/         # Static files (CSS, JS, images)
    └── templates/      # Jinja2 templates
```

## Installation

1. Clone the repository
```bash
git clone https://github.com/yourusername/crucible.git
cd crucible
```

2. Create and activate a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

## Running the Application

To run the development server:
```bash
python app.py
```

Or alternatively:
```bash
flask run
```

The application will be available at http://127.0.0.1:5000/

## Testing

To run tests:
```bash
pytest
```

## Deployment

For production deployment, consider using Gunicorn as a WSGI server:
```bash
gunicorn -w 4 -b 0.0.0.0:8000 app:app
```

## License

[MIT](LICENSE)
