# Import Flask class from flask package
from flask import Flask

# Create Flask application object
app = Flask(__name__)

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