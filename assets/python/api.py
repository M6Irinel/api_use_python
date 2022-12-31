from flask import Flask, jsonify
from flask_cors import CORS

import DB

app = Flask(__name__)

CORS(app)

@app.route('/select/<string:table>', methods=['GET'])
def select(table: str):
    return jsonify(DB.select(table))


@app.route('/insert/<string:table>/<string:columns>/<string:values>', methods=['PUT'])
def insert(table: str, columns: str, values: str):
    return DB.insert(table, columns, values)
        
app.run(port=8000)