from flask import Flask, render_template, request,redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cave', methods=['GET', 'POST'])
def cave():
    if request.method == 'POST':
        data = request.form.get ('data', '')
        return render_template('cave.html') 

if __name__ == '__main__':
    app.run(debug=True)

