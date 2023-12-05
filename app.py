import os
from flask import Flask, redirect, render_template, request
from examine import store1

from openpyxl import load_workbook



app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")


@app.route("/", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        f = request.files["Upload File"]
        # f.save("data/course1.xlsx")
        g = str(f)
        file_name = []
        file_name = g.split(" ")
        g = file_name[1]
        g = g.strip("''")
        f.save(f"data/{g}")
        workbook = load_workbook(filename=f"data/{g}")
        f_name = f"data/{g}"
        out1 = store1(workbook)
        os.remove(f_name)
        return f"{out1}\n"
    else:
        return render_template("index.html")


# @app.route("/place/", methods=["GET", "POST"])
# def get_place():
#     if request.method == "POST":
#         city_name = request.form.get("place")
#         place_name = find_stop_near(city_name)
#         return f"{city_name}: {place_name}."
#     else:
#         return render_template("place.html")



if __name__ == '__main__':
    app.run(debug=True)
