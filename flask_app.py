from flask import Flask, request, jsonify
import telebot
from bot import bot, send_message

app = Flask(__name__)

# Telegram webhook endpoint
@app.route(f"/{bot.token}", methods=["POST"])
def telegram_webhook():
    json_data = request.get_json()
    update = telebot.types.Update.de_json(json_data)
    bot.process_new_updates([update])
    return "OK", 200

# Mini App endpoint (Telegram WebApp)
@app.route("/app")
def mini_app_page():
    return "<h2>Hello from Mini App!</h2>"

# Example API endpoint for web app to talk to bot backend
@app.route("/api/send", methods=["POST"])
def api_send():
    data = request.json
    chat_id = data.get("chat_id")
    msg = data.get("msg")
    send_message(chat_id, msg)
    return jsonify({"status": "sent"})