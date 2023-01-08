from flask import Flask
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello():
    # Connect to the database
    conn = mysql.connector.connect(user='user', password='password', host='mysql', database='db')
    cursor = conn.cursor()
    
    # Read the current time from the database
    cursor.execute('SELECT NOW()')
    current_time = cursor.fetchone()[0]
    
    # Close the connection to the database
    cursor.close()
    conn.close()
    
    # Return the current time as the response
    return f'The current time is: {current_time}'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)