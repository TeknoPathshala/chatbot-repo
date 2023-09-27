from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample chatbot responses
responses = {
    "hello": "Hi there! How can I help you?",
    "bye": "Goodbye! Have a great day!",
    "default": "I'm just a simple chatbot. Ask me anything.",
}

@app.route("/", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data["message"].lower()

    response = responses.get(user_message, responses["default"])
    
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
