from flask import render_template
from flask import Flask

app = Flask(__name__)

class article:
    def __init__(self, url):
        self.url = url
        # note: change to grab the title by making a GET request
        self.title = "title here"

@app.route("/")
def urls():
    articles = [article("https://winesj.com"), article("https://connellyj.github.io/")]
    return render_template("index.html", articles = articles)

@app.route('/static/<path:path>')
def send_static(path):
    return send_from_directory('static', path)


if __name__ == '__main__':
    app.run()
