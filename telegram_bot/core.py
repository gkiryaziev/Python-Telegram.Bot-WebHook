import logging
import sys

from flask import Flask, request, jsonify

from telegram_bot.ngrok_api.core import get_ngrok_url
from telegram_bot.telegram_api.core import TelegramApi
from telegram_bot.telegram_api.parser import parse_text

# from flask_sslify import SSLify

#telegram bot token
TOKEN = "xxx"
telegram = TelegramApi(TOKEN)

# disable logging
log = logging.getLogger("werkzeug")
log.setLevel(logging.ERROR)
# log.disabled = True

app = Flask(__name__)
# sslify = SSLify(app)


@app.route("/")
def index():
    return "Ok"


@app.route("/webhook", methods=["POST", "GET"])
def webhook():
    if request.method == "POST":
        req = request.get_json()
        # print(req)
        if "message" in req and "text" in req["message"]:
            chat_id = req["message"]["chat"]["id"]
            message_text = req["message"]["text"]
            first_name = req["message"]["from"]["first_name"]
            language_code = req["message"]["from"]["language_code"]
            # some logic
            response_text = parse_text(message_text, first_name, language_code)
            if response_text is not None:
                telegram.send_message(chat_id, response_text, mode_html=True, save=True)
        return jsonify(req)
    return "Ok"


def compare_url():
    # 1. get url from ngrok and add route
    ngrok_url = get_ngrok_url()
    ngrok_url += "/webhook"
    print("ngrok: " + ngrok_url)
    # 2. get url from webhook
    webhook_url = telegram.get_webhook_info()["result"]["url"]
    print("webhook: " + webhook_url)
    # 3. compare url's, set webhook if not equal
    if ngrok_url != webhook_url:
        print("ngrok != webhook, setting up webhook url")
        telegram.set_webhook(ngrok_url, True)
        return False
    else:
        print("url's is equal, starting flask")
        return True


def main():
    try:
        compare = compare_url()
        while not compare:
            compare = compare_url()
        # 4. run flask
        app.run()
    except Exception as ex:
        print(ex)
        sys.exit(1)


if __name__ == "__main__":
    main()
