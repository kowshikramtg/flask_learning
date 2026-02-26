from flask import Flask

app=Flask(__name__)

# creating routes
@app.route('/')
def hello():
    return "hello world"
# create a new route for /index
@app.route('/index')
def index():
    return "hello index"

# Entering point of the file. debug = True makes save server after saving files.
if __name__ == '__main__':
    app.run(debug=True)