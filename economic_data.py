import sqlite3
from flask import Flask, render_template, request

# app = Flask(__name__, instance_relative_config=True) creates the Flask instance. 
# __name__ is the name of the current Python module. 
app = Flask(__name__)

# App Routing means mapping the URLs to a specific function that will handle the logic for that URL.
# In our application, the URL (“/”) is associated with the root URL.
@app.route('/')
def index():
    # open the connection to the database
    conn = sqlite3.connect('economic_data.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute("select * from countries")  # Corrected table name
    rows = cur.fetchall()
    conn.close()
    return render_template('index.html', rows=rows)

@app.route('/show/<CountryID>')
def show(CountryID):
    conn = sqlite3.connect('economic_data.db')
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    # get results from countries table for a specific CountryID
    cur.execute("select * from countries WHERE CountryID =?", (CountryID,))
    row = cur.fetchone()  # Fetching one row since CountryID should be unique
    conn.close()
    if row:
        return render_template('show.html', row=row, CountryName=row['CountryName'])
    else:
        return "Country not found", 404  # Proper error handling if no country is found




