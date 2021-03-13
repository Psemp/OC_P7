from flask import Flask, render_template, request, jsonify
from .script.question_processing import question_processing
from .models.question import Question


app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


@app.route('/process', methods=['GET', 'POST'])
def data_processing():

    user_query = request.form['question']
    user_question = Question()
    answer = question_processing(user_query, user_question)

    return jsonify({'answer': answer})


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')

    return response


if __name__ == "__main__":
    app.run(debug=True)
