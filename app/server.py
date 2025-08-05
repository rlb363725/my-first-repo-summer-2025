from flask import Flask, request, jsonify
from app.rps import determine_winner, VALID_OPTIONS
import random

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome to Rock, Paper, Scissors!"

@app.route("/play", methods=["POST"])
def play():
    user_choice = request.json.get("choice")
    if user_choice not in VALID_OPTIONS:
        return jsonify({"error": "Invalid choice"}), 400

    computer_choice = random.choice(VALID_OPTIONS)
    result = determine_winner(user_choice, computer_choice)

    return jsonify({
        "user_choice": user_choice,
        "computer_choice": computer_choice,
        "result": result
    })

if __name__ == "__main__":
    app.run(debug=True)
