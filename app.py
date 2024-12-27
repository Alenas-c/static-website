import os
import logging
from flask import Flask, render_template

# Initialize Flask application
app = Flask(__name__)

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("app.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Serve the homepage
@app.route('/')
def home():
    logger.info("Homepage accessed.")
    return render_template('index.html')

# Serve a sample static page
@app.route('/about')
def about():
    logger.info("About page accessed.")
    return render_template('about.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    logger.info("Starting the Flask app on port %s", port)
    app.run(debug=True, host='0.0.0.0', port=port)
