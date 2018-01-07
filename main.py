from flask import Flask, render_template, request
from jsonHandle import create_simple_json_hello, handle_json_post

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/json', methods=['GET'])
def hello_json_get():
    return create_simple_json_hello()


@app.route('/json', methods=['POST'])
def hello_json_post():
    return handle_json_post(request)


if __name__ == '__main__':
    app.run(debug=True)
