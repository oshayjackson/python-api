from flask import Flask, render_template, request
from urls import URL

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def index():
    data = None

    if request.method == "POST":
        query = request.form.get("search_query")
        if query:
            url_instance = URL(query)
            data = url_instance.data

    return render_template("index.html", data=data)


if __name__ == "__main__":
    app.run(debug=True)
