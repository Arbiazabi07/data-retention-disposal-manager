import os
import logging
from datetime import date, datetime
from flask import Flask, request, jsonify

app = Flask(__name__)
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

GROQ_API_KEY = os.environ.get('GROQ_API_KEY', '')


def get_groq_client():
    if not GROQ_API_KEY:
        return None
    try:
        from groq import Groq
        return Groq(api_key=GROQ_API_KEY)
    except Exception as e:
        logger.warning("Failed to initialize Groq client: %s", e)
        return None


def compute_compliance_score(expiry_date_str, status):
    try:
        expiry = datetime.strptime(expiry_date_str, '%Y-%m-%d').date()
        days_remaining = (expiry - date.today()).days
        if days_remaining < 0:
            return 0.1
        if days_remaining < 30:
            return 0.4
        if days_remaining < 90:
            return 0.6
        return 0.9
    except Exception:
        return 0.5 if status == 'ACTIVE' else 0.3


@app.route('/health')
def health():
    return jsonify({'status': 'ok', 'ai_enabled': bool(GROQ_API_KEY)})


@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    if not data:
        return jsonify({'error': 'No data provided'}), 400

    name = data.get('name', 'Unknown')
    data_type = data.get('dataType', 'Unknown')
    department = data.get('department', 'Unknown')
    retention_years = data.get('retentionYears', 0)
    expiry_date = data.get('expiryDate', '')
    status = data.get('status', 'ACTIVE')

    score = compute_compliance_score(expiry_date, status)
    client = get_groq_client()

    if not client:
        description = (
            f"This {data_type} record from the {department} department has a "
            f"{retention_years}-year retention period expiring on {expiry_date}. "
            f"Current compliance status: {status}."
        )
        return jsonify({'aiDescription': description, 'aiScore': score})

    try:
        prompt = (
            f"Analyze this data record and write a concise 1-2 sentence compliance summary. "
            f"Be specific, professional, and mention the retention period and any risk.\n\n"
            f"Record: {name}\nType: {data_type}\nDepartment: {department}\n"
            f"Retention: {retention_years} years\nExpiry: {expiry_date}\nStatus: {status}\n\n"
            f"Output only the description text, no labels or formatting."
        )
        response = client.chat.completions.create(
            model="llama3-8b-8192",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=150,
            temperature=0.3,
        )
        ai_description = response.choices[0].message.content.strip()
        return jsonify({'aiDescription': ai_description, 'aiScore': score})
    except Exception as e:
        logger.error("Groq API error: %s", e)
        return jsonify({'error': 'AI service temporarily unavailable'}), 503


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
