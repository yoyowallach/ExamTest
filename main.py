# main.py

from flask import Flask, render_template, request, redirect, url_for
import uuid  # For generating UUIDs
import sqlite3  # For SQLite database operations

app = Flask(__name__)

# Function to establish database connection
def get_db_connection():
    conn = sqlite3.connect('exams.db')
    conn.row_factory = sqlite3.Row
    return conn

# Routes
@app.route('/')
def index():
    return render_template('index.html')

# Admin portal routes
@app.route('/admin/login', methods=['GET', 'POST'])
def admin_login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Check username and password against database
        # Redirect to admin dashboard if credentials are correct
        return redirect(url_for('admin_dashboard'))
    return render_template('admin_login.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    # Display admin dashboard
    return render_template('admin_dashboard.html')

# Test taker portal routes
@app.route('/exam/<uuid>')
def take_exam(uuid):
    # Display exam form for test taker
    return render_template('exam_form.html')

@app.route('/exam/<uuid>/submit', methods=['POST'])
def submit_exam(uuid):
    # Submit exam answers and calculate score
    return redirect(url_for('exam_result'))

@app.route('/exam/<uuid>/result')
def exam_result():
    # Display exam result
    return render_template('exam_result.html')

if __name__ == '__main__':
    app.run(debug=True)
