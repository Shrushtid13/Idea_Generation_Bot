#!/bin/sh
# run.sh — Start both Flask (via Gunicorn) and Streamlit

echo "🚀 Starting Flask API (Gunicorn) and Streamlit UI..."

# Start Flask API (backend) on port 5000 using Gunicorn
gunicorn --workers=1 --threads=10 --timeout=120 --bind 0.0.0.0:5000 wsgi:app &

# Wait for Flask to start up
sleep 5

# Start Streamlit (frontend) on port 8501
streamlit run streamlit_app.py --server.port=8501 --server.address=0.0.0.0
