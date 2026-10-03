# Plant Disease AI Drone

A Flask-based project for detecting plant diseases from images captured by a drone or uploaded through the web interface.

## Project structure

- `app.py` – Flask application entry point
- `model/` – trained model files and model logic
- `dataset/` – raw and processed dataset assets
- `disease_data/` – disease labels, mappings, and metadata
- `templates/` – HTML templates
- `static/` – CSS, JavaScript, and uploaded image files
- `drone/` – drone flight and capture logic
- `tests/` – application tests
- `docs/` – project documentation

## Getting started

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/macOS
   venv\Scripts\activate     # Windows
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   python app.py
   ```
4. Open the browser at `http://127.0.0.1:5000`

## Notes

This is a starter scaffold for a plant disease detection project. You can extend the model, dataset, and drone modules as the project grows.
