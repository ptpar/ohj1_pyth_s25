import mysql.connector
from flask import Flask
from asetukset import own_username , own_password

cnx = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    database='flight_game',
    user=own_username,
    password=own_password,
    autocommit=True
    )
app = Flask(__name__)
@app.route('/kenttä/<icao>')
def airport(icao):
    sql = 'select ident,name,municipality from airport where ident=%s'
    cursor = cnx.cursor(dictionary=True)
    cursor.execute(sql, (icao,))
    result = cursor.fetchone()
    return {'ICAO': result['ident'], 'Name': result['name'], 'Municipality': result['municipality']}

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)