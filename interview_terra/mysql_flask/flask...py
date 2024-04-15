

from flask import Flask, render_template

app = Flask(__name__)
@app.route("/")
def home():
    return render_template('pavan.html')



# @app.route("/")
# def home():
#     return render_template("pavan.html")



# @app.route("/salvador/<name>")
# def salvador(name):
#     return "Hello, Salvador"+name


if __name__ == "__main__":
    app.run(debug=True)