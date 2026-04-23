# Import Flask class from flask package
from flask import Flask

# Import the describe blueprint
from routes.describe import describe_bp

from routes.recommend import recommend_bp


# Create Flask application object
app = Flask(__name__)

# Register the /describe route
app.register_blueprint(describe_bp)
app.register_blueprint(recommend_bp)

# Create a simple route to check if server is running
@app.route('/health')
def health():

    # Return JSON response
    return {
        "status": "working"
    }

# Start Flask server
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)