from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', active='home')

@app.route('/about')
def about():
    return render_template('about.html', active='about')

@app.route('/dashboard01')
def dashboard01():
    return render_template('dashboard01.html', active='dashboard01')

@app.route('/dashboard02')
def dashboard02():
    return render_template('dashboard02.html', active='dashboard02')

@app.route('/story')
def story():
    return render_template('story.html', active='story')

if __name__ == '__main__':
    app.run(debug=True)