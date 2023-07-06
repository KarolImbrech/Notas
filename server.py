from flask import Flask, render_template
from database.estudiante import consult_est

app = Flask(__name__, static_url_path="", static_folder='frontend/statics', template_folder='frontend/templates')

@app.route("/")
def func_home():
    return render_template("home.html")

@app.route("/profesor_page")
def profesor_page():
    return render_template("profesor_page.html")

@app.route("/estudiante_page")
def estudiante_page():
    return render_template("estudiante_page.html")

@app.route("/consult_est", methods=["POST"])
def func_consult_est():
    return consult_est()

if __name__ == "__main__":
    host = "127.0.0.1"
    port = 3000
    app.run(host, port, debug=True) 