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
        return render_template("list.html", len=len(out1), out1=out1)
        # return out1
        # return "\n".join(out1)
    else:
        return render_template("index.html")
    
# @app.post("/result/")
# @app.route("/result", methods=["GET", "POST"])
# def feedback():
#     if request.method == "POST":


if __name__ == '__main__':
    app.run(debug=True)
