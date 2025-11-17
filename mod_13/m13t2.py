import mysql.connector
from flask import Flask

cnx = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user='user',
    password='password',
    autocommit=True
    )
app = Flask(__name__)
@app.route('/kenttä/<icao>')
def airportsearch(icao):
    sql = 'select ident as ICAO,name as Name,municipality as Municipality from airport where ident=%s'
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    return result

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)