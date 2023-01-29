from flask import Flask, render_template, request
app = Flask(__name__, template_folder='templates', static_folder='templates/assets')

@app.route('/')
def form():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def result():
    return render_template('result.html', result=0)

if __name__ == '__main__':
    app.run(debug=False)