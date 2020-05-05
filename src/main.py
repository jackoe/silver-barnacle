from flask import Flask, request, render_template

app = Flask(__name__)

class article:
    def __init__(self, url):
        self.url = url
        # note: change to grab the title by making a GET request
        self.title = "title here"

articles = [article("https://winesj.com"), article("https://connellyj.github.io/")]

@app.route("/")
def urls():
    return render_template("index.html", articles = articles)

@app.route("/add", methods=["POST"])
def add_url():
    articles.append(article(request.get_json()["url"]))
    return "okay"

@app.route("/static/<path:path>")
def send_static(path):
    return send_from_directory("static", path)

if __name__ == "__main__":
    app.run()
