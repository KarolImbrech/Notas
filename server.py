from flask import Flask, render_template

app = Flask(__name__, static_url_path="", static_folder='frontend/statics', template_folder='frontend/templates')

@app.route("/")
def func_home():
    return render_template("home.html")

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 3000
    app.run(host, port, debug=True) 