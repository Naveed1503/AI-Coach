import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# API URL for aptitude questions (replace with a better API if needed)
API_URL = "https://opentdb.com/api.php?amount=1&category=9&type=multiple"

@app.route('/')
def aptitude():
    return render_template('aptitude_round.html')

@app.route('/get_question', methods=['GET'])
def get_question():
    response = requests.get(API_URL)
    if response.status_code == 200:
        data = response.json()
        question_data = data['results'][0]
        
        question = question_data['question']
        options = question_data['incorrect_answers']
        correct_answer = question_data['correct_answer']
        options.append(correct_answer)  # Adding correct answer to options
        
        return jsonify({"question": question, "options": options, "answer": correct_answer})
    else:
        return jsonify({"error": "Failed to fetch question"})

if __name__ == '__main__':
    app.run(debug=True, port=5001)
