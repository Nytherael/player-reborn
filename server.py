from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
@app.after_request
def after_request(response):
    response.headers.add("Access-Control-Allow-Origin", "*")
    return response

@app.route("/status")
def all_status():
    discord = requests.get("DISCORD_API_KEY_HERE").json()
    return {
        "discord_online": discord["presence_count"],
        "minecraft": {
            "players": 2,
            "status": "online"
        }
    }

if __name__ == "__main__":
    app.run(port=5000)