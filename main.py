from flask import Flask, render_template,redirect, url_for

app=Flask(__name__)

@app.route("/game")
def gamepage():
    return render_template("start.html")

if __name__=="__main__":
    app.run(debug=True)