from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess

app = Flask(__name__)
CORS(app)

@app.route('/scan', methods=['POST'])
def scan_code():

    data = request.json
    folder = data.get("folder", "")

    if not folder:
        return jsonify({
            "error": "Folder path missing"
        }), 400

    try:
        result = subprocess.check_output(
            ["bandit", "-r", folder, "-f", "json"],
            text=True
        )

        return jsonify({
            "status": "success",
            "report": result
        })

    except subprocess.CalledProcessError as e:
        return jsonify({
            "status": "failed",
            "error": str(e)
        })

if __name__ == '__main__':
    app.run(debug=True)