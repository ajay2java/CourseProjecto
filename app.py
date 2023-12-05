from flask import Flask, redirect, render_template, request
from examine import store1



app = Flask(__name__)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html")

# @app.route('/')
# def hello():
#     return render_template("index.html")

# @app.route('/upload', methods=['GET', 'POST'])
@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['Upload File']
        # f.save('/var/www/uploads/uploaded_file.csv')
        store1(f)
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
