from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello world'

@app.route('/home')
def home():
    return 'Home'



if __name__ == '__main__':
    app.run()