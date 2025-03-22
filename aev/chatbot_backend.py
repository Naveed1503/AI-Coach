from flask import Flask, request, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)

# Replace this with your actual OpenRouter API key
OPENROUTER_API_KEY = "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"

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "model": "openai/gpt-3.5-turbo",  # You can also use "mistralai/mixtral-8x7b" or "anthropic/claude-2"
        "messages": [
            {"role": "system", "content": "You are a helpful AI coach that guides users in interview preparation."},
            {"role": "user", "content": user_message}
        ]
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=payload)
        result = response.json()
        reply = result['choices'][0]['message']['content']
        return jsonify({'response': reply})
    except Exception as e:
        print("Error:", str(e))
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
