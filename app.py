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
        g = str(f)

        # We do the next 4-Lines below to isolate the actual name of the file, from the excess wording. The result of this will be ____.xlsx
        file_name = []
        file_name = g.split(" ")
        g = file_name[1]
        g = g.strip("''")

        # These two if-statements check for any errors, and report them to the 404.html for the proper output.
        if "data/" + g == "data/":
            return render_template("404.html")
        if ".xlsx" not in g:
            return render_template("404.html")
        f.save(f"data/{g}")
        workbook = load_workbook(filename=f"data/{g}")
        f_name = f"data/{g}"
        out1 = store1(workbook)
        #This will remove the entered user file to clear up the space.
        os.remove(f_name)
        # sends out1 variable to list.html to display it in a better visual manner.
        return render_template("list.html", len=len(out1), out1=out1)
    else:
        return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
