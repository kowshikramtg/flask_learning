from flask import Flask, render_template, request

app=Flask(__name__)

@app.route('/')
def hello():
    return "hello world"

@app.route('/success/<int:score>')
def success(score):
    res=""
    if score>=35:
        res="PASS"
    else:
        res="FAIL"
    return render_template('result.html', results=res)

@app.route('/successers/<int:score>')
def successers(score):
    res=""
    if score>=35:
        res="PASSED"
    else:
        res="FAILED"
    exp={'score': score, 'res': res}

    return render_template('result1.html', results = exp)

@app.route('/successif/<int:score>')
def successif(score):
    return render_template('result.html', results=score)


if __name__ == '__main__':
    app.run(debug=True)