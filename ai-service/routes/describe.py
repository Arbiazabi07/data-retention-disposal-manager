# Import Blueprint and request for API handling
from flask import Blueprint, request

# Import datetime to add timestamp
from datetime import datetime

# Create blueprint
describe_bp = Blueprint('describe', __name__)

# Create POST endpoint
@describe_bp.route('/describe', methods=['POST'])
def describe():

    # Read JSON input
    data = request.get_json()

    # Validate input
    if not data:
        return {
            "error": "Request body is required"
        }, 400

    record_type = data.get("recordType")
    retention_period = data.get("retentionPeriod")
    risk_level = data.get("riskLevel")

    # Validate required fields
    if not record_type or not retention_period or not risk_level:
        return {
            "error": "recordType, retentionPeriod and riskLevel are required"
        }, 400

    try:
        # TEMPORARY (replace later with Groq call)
        description = (
            f"{record_type} with {risk_level} risk should be securely retained for "
            f"{retention_period} before disposal."
        )

        return {
            "description": description,
            "generated_at": datetime.utcnow().isoformat(),
            "is_fallback": False
        }

    except Exception:
        # Fallback response if AI fails later
        return {
            "description": "AI service unavailable",
            "generated_at": datetime.utcnow().isoformat(),
            "is_fallback": True
        }