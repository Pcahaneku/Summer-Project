from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
        return render_template('homepage.html')

@app.route('/Register With Us')
def registration():
         return render_template('registrationpage.html')

@app.route('/timetable')
def timetable():
         return render_template('timetable.html')

@app.route('/submit')
def submit():
        return render_template('submit.html')

if __name__ == '__main__':
        app.run(debug=True)