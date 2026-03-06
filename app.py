from flask import Flask, jsonify

app = Flask(__name__)

# Health check endpoint
@app.route('/health')
def health():
    return jsonify({
        "status": "UP",
        "message": "Application is running"
    }), 200


# API endpoint
@app.route('/api/data')
def get_data():
    return jsonify({
        "name": "Sachin",
        "role": "DevOps Engineer",
        "message": "Hello from Flask API"
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
