from flask import Flask, render_template, request, jsonify
import Bot

bot = Bot.ChatBot()


Bot = Flask(__name__)


@Bot.get("/")
def index_get():
    return render_template("base.html")


@Bot.post("/predict")
def predict():
    txt = request.get_json().get("message")

    bot.user_input(txt)

    response = bot.bot_response()

    message = {"answer": response}

    return jsonify(message)


if __name__ == "__main__":
    Bot.run(debug=True)
