# Import Blueprint so that this route can be added to Flask
# Import request so we can read the JSON body sent by the user
from flask import Blueprint, request

# Create a blueprint named 'describe'
# Blueprint helps us keep this route in a separate file
describe_bp = Blueprint('describe', __name__)

# Create the API endpoint:
# URL -> /describe
# Method -> POST
@describe_bp.route('/describe', methods=['POST'])
def describe():

    # Read the JSON body from the request
    # Example:
    # {
    #   "recordType": "Employee Data",
    #   "retentionPeriod": "5 years",
    #   "riskLevel": "High"
    # }
    data = request.get_json()

    # If no JSON body is sent, return error
    if not data:

        # Return JSON response with HTTP status 400
        return {
            "error": "Request body is required"
        }, 400

    # Get recordType from the JSON body
    record_type = data.get("recordType")

    # Get retentionPeriod from the JSON body
    retention_period = data.get("retentionPeriod")

    # Get riskLevel from the JSON body
    risk_level = data.get("riskLevel")

    # Check whether any required field is missing
    if not record_type or not retention_period or not risk_level:

        # Return validation error if any field is missing
        return {
            "error": "recordType, retentionPeriod and riskLevel are required"
        }, 400

    # Created a temporary description manually
    
    description = (
        f"{record_type} with {risk_level} risk should be securely retained for "
        f"{retention_period} before disposal."
    )

    # Return the generated description as JSON
    return {
        "description": description
    }