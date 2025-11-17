from flask import Flask
#request, jsonify
from classes.alkuluku import alkuluku

app = Flask(__name__)
@app.route('/alkuluku/<int:luku>')
def hae_alkuluku(luku):
    prime = alkuluku(luku)
    vastaus = {"Number":luku, "isPrime":prime}
    return vastaus
"""
def alkuluku(luku):
    prime = True
    if luku <= 1:
        prime = False
    else:
        for i in range(2, luku // 2):
            if luku % i == 0:
                prime = False
                break
    vastaus = {"Number":luku, "isPrime":prime}
    return vastaus
"""


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
