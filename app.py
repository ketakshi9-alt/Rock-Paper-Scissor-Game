from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)

choices = ["rock", "paper", "scissors"]

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
        (user == "paper" and computer == "rock") or \
        (user == "scissors" and computer == "paper"):
        return "user"
    else:
        return "computer"

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/play", methods=["POST"])
def play():
    data = request.get_json()
    user = data.get("user", "").lower()
    computer = random.choice(choices)

    if user not in choices:
        return jsonify({"error": "Invalid input"}), 400

    winner = get_winner(user, computer)

    return jsonify({
        "user": user,
        "computer": computer,
        "winner": winner
    })

if __name__ == "__main__":
    app.run(debug=True)