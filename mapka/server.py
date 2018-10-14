from flask import Flask, jsonify, make_response
from database import Database

app = Flask(__name__)

@app.route("/stops/<city>")
def get_city(city):

    nodes = {key: Database.NodesGroups[key] for key in Database.Cities[city] if Database.NodesCounter[key] > 0}

    data = {
        'nodes': nodes,
        'routes': Database.routes_per_nodes(nodes)
    }

    resp = make_response(jsonify(data))
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

if __name__ == '__main__':
    app.run(debug=True)
