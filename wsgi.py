from app import app  # Import the Flask app instance from app.py

if __name__ == "__main__":
    # Useful for running locally (not used in production)
    app.run(host="0.0.0.0", port=5000, debug=True)