# ============================================================
# wsgi.py — Production entry point
# ============================================================
# gunicorn uses this file to find the Flask app object.
# Start production server with:
#   gunicorn wsgi:app
# Or with workers + port:
#   gunicorn --workers 2 --bind 0.0.0.0:$PORT wsgi:app
# ============================================================

from app import app

if __name__ == "__main__":
    app.run()
