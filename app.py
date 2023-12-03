from flask import Flask, redirect, render_template, request
from examine import Concentration



app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

@app.route('/')
def hello():
    return render_template("index.html")

@app.route("/place/", methods=["GET", "POST"])
def get_place():
    if request.method == "POST":
        city_name = request.form.get("place")
        place_name = find_stop_near(city_name)
        return f"{city_name}: {place_name}."
    else:
        return render_template("place.html")

# @app.route('/place/')
# def place_get():
#     return render_template("place.html")

# @app.route('/place/')
# def place():
#     place_name = request.form.get("place")
#     res1 = find_stop_near(place_name)
#     return f"{res1}"


if __name__ == '__main__':
    app.run(debug=True)
