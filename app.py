from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

conn = sqlite3.connect('expenses.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS expenses (
    id INTEGER PRIMARY KEY,
    date TEXT NOT NULL,
    description TEXT NOT NULL,
    amount REAL NOT NULL,
    category TEXT NOT NULL
)''')
conn.commit()
conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    c.execute("SELECT * FROM expenses")
    expenses = c.fetchall()
    conn.close()
    return render_template('index.html', expenses=expenses)

@app.route('/add', methods=['POST'])
def add_expense():
    conn = sqlite3.connect('expenses.db')
    c = conn.cursor()
    date = request.form['date']
    description = request.form['description']
    amount = request.form['amount']
    category = request.form['category']
    c.execute("INSERT INTO expenses (date, description, amount, category) VALUES (?, ?, ?, ?)", (date, description, amount, category))
    conn.commit()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(debug=True)
