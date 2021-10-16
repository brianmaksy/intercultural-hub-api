from flask import Flask, render_template, jsonify
from data.bridge_builders import bridge_builders
from data.hubs import hubs


app = Flask(__name__)


# all bridge builders 
@app.route("/bridge-builders")
def bridgeBuildersHandler():
     return jsonify(bridge_builders)

# return specific bridge builder with 
@app.route("/bridge-builders/<id>")
def bridgeBuildersIDHandler(id):
    # loop through list of bridge builders 
    bridgeBuilder = False 
    for entry in bridge_builders:
        if entry.get("id") == id:
            bridgeBuilder = entry 
    return entry 
    
# return the categories 
@app.route("/search-culture")
def searchCulturesHandler():
    culture_tokens = {c for expert in bridge_builders for c in expert["culture"]}
    culture_tokens = list(culture_tokens)
    return jsonify(culture_tokens)

# hubs: just to return list of hubs 
@app.route("/hubs")
def hubsHandler():
    return jsonify(hubs)

if __name__ == "__main__":
    app.run(debug=True)