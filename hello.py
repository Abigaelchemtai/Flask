from flask import Flask
app=Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/name')
def myname():
    return 'Am Abbie!'

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' %name

if __name__=='__main__':
    app.run(debug=True)