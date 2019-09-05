import json
from os import environ as env

from dotenv import load_dotenv
from flask import Flask
from flask import request
import requests

load_dotenv()

LINE_CHANNEL_ACCESS_TOKEN = env.get("LINE_CHANNEL_ACCESS_TOKEN")
LINE_USER_ID = env.get("LINE_USER_ID")
BASE_URL = "https://api.line.me/v2/bot/message/push"
HEADER = {
    "Content-Type": "application/json",
    "Authorization": "Bearer " + LINE_CHANNEL_ACCESS_TOKEN,
}

webhook = Flask(__name__)


@webhook.route("/answer")
def answer():
    message = {"to": LINE_USER_ID, "messages": [{"type": "text", "text": "42"}]}
    res = requests.post(BASE_URL, json.dumps(message), headers=HEADER)
    return res.json()


@webhook.route("/api/v1/message")
def message():
    dic, keys = request.args, request.args.keys()
    message_text = ""
    for key in keys:
        message_text += key + ": " + dic.get(key) + "\n"
    message = {
        "to": LINE_USER_ID,
        "messages": [{"type": "text", "text": message_text.rstrip("\n")}],
    }
    res = requests.post(BASE_URL, json.dumps(message), headers=HEADER)
    return res.json()


if __name__ == "__main__":
    webhook.run(host="0.0.0.0", port=env.get("PORT"))
