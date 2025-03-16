"""
Main application file for the Topic to MP3/Video Generator.
This file initializes the Flask application and registers all blueprints.
"""

from flask import Flask, render_template, send_from_directory
import os
from utils.config import SECRET_KEY
from routes.api import api_bp
from routes.pages import pages_bp

def create_app():
    """
    Create and configure the Flask application.
    
    Returns:
        Flask: The configured Flask application.
    """
    app = Flask(__name__, static_folder='static')

    # Configure app
    app.config['SECRET_KEY'] = SECRET_KEY
    app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.config['PREFERRED_URL_SCHEME'] = 'https'

    # Register blueprints
    app.register_blueprint(api_bp)
    app.register_blueprint(pages_bp)

    # Static file serving
    @app.route('/static/<path:path>')
    def serve_static(path):
        return send_from_directory('static', path)

    # Catch-all route for SPA routing
    @app.route('/<path:path>')
    def catch_all(path):
        # Try to serve as a template first
        try:
            return render_template(f"{path}.html")
        except:
            # If template not found, try to serve as a static file
            try:
                return app.send_static_file(path)
            except:
                # If file not found, return the index.html (for SPA routing)
                return render_template('home.html')

    return app

# Create the application instance
app = create_app()

# For local development only
if __name__ == '__main__':
    app.run(debug=True, port=5000)
