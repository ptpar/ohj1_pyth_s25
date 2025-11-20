from flask import Flask, Response
import json
from classes.alkuluku import alkuluku

app = Flask(__name__)
@app.route('/alkuluku/<luku>')
#tai: <int:luku>
#'/alkuluku/<luku>'
def hae_alkuluku(luku):
    try:
        prime = alkuluku(int(luku))
        status_code = 200
        result = {"Status": status_code, "Number":luku, "isPrime":prime}
    except ValueError:
        status_code = 400
        result = {"Status": status_code, "Explanation": "Bad request. Incorrect number."}
    json_result = json.dumps(result)
    return Response(response=json_result, status=status_code, mimetype='application/json')

@app.errorhandler(404)
def page_not_found(error):
    result = {"Status": error.code, "Explanation": error.description}
    json_result2 = json.dumps(result)
    return Response(response=json_result2, status=404, mimetype='application/json')


if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
