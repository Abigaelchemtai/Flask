from flask import Flask, request, redirect, url_for
app = Flask(__name__)

@app.route('/Welcome/<name>')
def Welcome (name):
    return 'Welcome %s' %name 

@app.route('/login', methods=['POST','GET'])
def login():
    if request.method == 'POST':
        user=request.form['nm']
        return redirect(url_for('Welcome', name=user))
    else:
        user=request.args.get('nm')
        return redirect(url_for('Welcome', name=user))

if __name__ == "__main__":
    app.run(debug=True)


