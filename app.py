from flask import Flask, render_template, request

app=Flask(__name__)

# creating routes
@app.route('/')
def hello():
    return "<html><body><h2>Hello World</h2></body></html>"
# create a new route for /index
@app.route('/index', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/form', methods=['GET', 'POST'])
def form():
    if request.method=='POST':
        name=request.form['name']
        return f'Hello {name}'
    return render_template('form.html')

# Entering point of the file. debug = True,  makes server save after saving files.
if __name__ == '__main__':
    app.run(debug=True)