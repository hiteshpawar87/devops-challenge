from flask import Flask, jsonify, request
import socket
from datetime import datetime

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_time():
    client_ip = request.remote_addr
    timestamp = datetime.utcnow().isoformat() + "Z"
    return jsonify({
        "timestamp": timestamp,
        "client_ip": client_ip,
        "hostname": socket.gethostname()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
