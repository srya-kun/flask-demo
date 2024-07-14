from flask import Flask

app = Flask(__name__)
@app.route('/')

def start():
    return '<h1 style="font-color:red">Hello World!</h1>'

app.run(host='0.0.0.0', port=8080, debug= True)