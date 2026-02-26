from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/sobre")
def sobre():
    return render_template("sobre.html")

@app.route("/astronomia")
def astronomia():
    return render_template("astronomia.html")

@app.route("/quimica")
def quimica():
    return render_template("quimica.html")

@app.route("/biologia")
def biologia():
    return render_template("biologia.html")

if __name__ == "__main__":
    app.run(debug=True)
