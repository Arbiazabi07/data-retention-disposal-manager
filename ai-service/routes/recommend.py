# Import Blueprint for route creation
# Import request to read JSON input
from flask import Blueprint, request

# Created blueprint for recommend endpoint
recommend_bp = Blueprint('recommend', __name__)

# Created POST endpoint: /recommend
@recommend_bp.route('/recommend', methods=['POST'])
def recommend():

    # Read JSON body from request
    data = request.get_json()

    # Check if request body is missing
    if not data:
        return {
            "error": "Request body is required"
        }, 400

    # Temporary static recommendations (will be replaced by Groq later)
    return [

        # Recommendation 1
        {
            "action_type": "Archive",
            "description": "Move inactive records to secure storage.",
            "priority": "High"
        },

        # Recommendation 2
        {
            "action_type": "Review",
            "description": "Review records nearing their retention period.",
            "priority": "Medium"
        },

        # Recommendation 3
        {
            "action_type": "Delete",
            "description": "Delete records after retention period expires.",
            "priority": "Low"
        }
    ]