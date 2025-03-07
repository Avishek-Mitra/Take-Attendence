from flask import Flask, render_template

app = Flask(__name__)

# Route for the index page
@app.route('/')
def index():
    return render_template('index.html')

# Route for the take page
@app.route('/take')
def take():
    return render_template('take.html')

if __name__ == '__main__':
    app.run(debug=True)
