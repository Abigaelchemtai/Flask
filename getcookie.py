from flask import Flask

app=Flask(__name__)

@app.route('/getcookie')
def getcookie():
    name=request.cookies.get('userID')
    return '<h1>Welcome '+name+'</h1>'