# main.py

from flask import Flask, render_template

app = Flask(__name__)

# Routes
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/admin/login')
def admin_login():
    return render_template('admin_login.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin_dashboard.html')

@app.route('/exam/<uuid>')
def take_exam(uuid):
    return render_template('exam_form.html')

@app.route('/exam/<uuid>/result')
def exam_result(uuid):
    return render_template('exam_result.html')

if __name__ == '__main__':
    app.run(debug=True)
