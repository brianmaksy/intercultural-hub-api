from flask import Flask, render_template, jsonify, request
from geopy.distance import distance
from data.bridge_builders import bridge_builders
from data.hubs import hubs


app = Flask(__name__)


# all bridge builders who match filters
@app.route("/bridge_builders")
def bridgeBuildersHandler():
    filter_params = request.args.to_dict(flat=False)

    def _is_in_filter(bridge_builder):
        for culture in filter_params.get("culture", []):
            if culture in bridge_builder["cultures"]:
                return True

        for ministry_area in filter_params.get("ministry_area", []):
            if ministry_area in bridge_builder["ministry_areas"]:
                return True

        for church in filter_params.get("church", []):
            if church == bridge_builder["church"]:
                return True

        if (
            "latitude" in filter_params
            and "longitude" in filter_params
            and "distance_km" in filter_params
        ):
            search_location = (
                filter_params["latitude"][0],
                filter_params["longitude"][0],
            )
            bridge_builder_location = (
                bridge_builder["latitude"],
                bridge_builder["longitude"],
            )
            if distance(search_location, bridge_builder_location).km <= float(
                filter_params["distance_km"][0]
            ):
                return True

        return False

    filtered_bridge_builders = [
        bridge_builder
        for bridge_builder in bridge_builders
        if _is_in_filter(bridge_builder)
    ]

    return jsonify(filtered_bridge_builders)


# return specific bridge builder with
@app.route("/bridge_builders/<id>")
def bridgeBuildersIDHandler(id):
    # loop through list of bridge builders
    bridgeBuilder = None
    for entry in bridge_builders:
        if entry.get("id") == id:
            bridgeBuilder = entry
            break
    return jsonify(bridgeBuilder)


# return the cultures which match the search term
@app.route("/search_culture")
def searchCulturesHandler():
    term = request.args.get("term")
    culture_tokens = {
        c
        for expert in bridge_builders
        for c in expert["cultures"]
        if term.lower() in c.lower()
    }
    culture_tokens = list(culture_tokens)
    return jsonify(culture_tokens)


# hubs: just to return list of hubs
@app.route("/hubs")
def hubsHandler():
    return jsonify(hubs)


# hubs: just to return list of hubs
@app.route("/ministry_areas")
def ministryAreasHandler():
    return jsonify(
        list(
            {
                ministry_area
                for expert in bridge_builders
                for ministry_area in expert["ministry_areas"]
            }
        )
    )


if __name__ == "__main__":
    app.run(debug=True)