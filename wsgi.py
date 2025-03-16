from app import app

# This file is used by WSGI servers like Gunicorn
# For Vercel deployment, index.py is used instead

if __name__ == '__main__':
    app.run() 