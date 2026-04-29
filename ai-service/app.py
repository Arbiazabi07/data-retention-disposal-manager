# Import Flask class from flask package
from flask import Flask

# Import the describe blueprint
from routes.describe import describe_bp

from routes.recommend import recommend_bp

from routes.report import report_bp

# Create Flask application object
app = Flask(__name__)

# Register the /describe route
app.register_blueprint(describe_bp)
app.register_blueprint(recommend_bp)
app.register_blueprint(report_bp) 

# Create a simple route to check if server is running
@app.route('/health')
def health():

    # Return JSON response
    return {
        "status": "working"
    }
@app.after_request
def add_security_headers(response):
    
    # Prevent clickjacking
    response.headers['X-Frame-Options'] = 'SAMEORIGIN'
    
    # Prevent MIME sniffing
    response.headers['X-Content-Type-Options'] = 'nosniff'
    
    # Enable basic XSS protection
    response.headers['X-XSS-Protection'] = '1; mode=block'
    
    # Control content sources
    response.headers['Content-Security-Policy'] = "default-src 'self'"
    
    return response
# Start Flask server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)