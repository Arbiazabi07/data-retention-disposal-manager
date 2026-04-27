# Import Blueprint and request
from flask import Blueprint, request

# Import datetime for timestamp
from datetime import datetime

# Create blueprint
report_bp = Blueprint('report', __name__)

# Create POST endpoint
@report_bp.route('/generate-report', methods=['POST'])
def generate_report():

    # Read request JSON
    data = request.get_json()

    # Validate input
    if not data:
        return {
            "error": "Request body is required"
        }, 400

    try:
        # Temporary static response (replace with Groq later)
        report = {
            "title": "Data Retention Summary",

            "summary": "This report summarizes current data retention status.",

            "overview": "Most records are within retention period, but some require review.",

            "key_items": [
                "12 records nearing expiration",
                "5 high-risk records require attention"
            ],

            "recommendations": [
                "Archive inactive records",
                "Review high-risk data",
                "Delete expired records after approval"
            ]
        }

        return {
            "report": report,
            "generated_at": datetime.utcnow().isoformat(),
            "is_fallback": False
        }

    except Exception:
        return {
            "report": {},
            "generated_at": datetime.utcnow().isoformat(),
            "is_fallback": True
        }