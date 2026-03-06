from flask import Flask, jsonify

app = Flask(__name__)

# Health check endpoint
@app.route('/health')
def health():
    return jsonify({
        "status": "UP",
        "message": "Application is running faster than ever!"
    }), 200


# API endpoint
@app.route('/api/data')
def get_data():
    return jsonify({
        "name": "Sachin",
        "role": "DevOps Engineer",
        "message": "Hello from Flask API"
    }), 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

# New API endpoint (Feature branch change)
@app.route('/api/time')
def get_time():
    from datetime import datetime
    return jsonify({
        "current_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "message": "Current server time"
    })


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8080)