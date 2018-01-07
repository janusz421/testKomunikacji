from flask import Flask, render_template
from jsonHandle import create_simple_json_hello

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('home.html')


@app.route('/json')
def hello_json():
    return create_simple_json_hello()


if __name__ == '__main__':
    app.run()
