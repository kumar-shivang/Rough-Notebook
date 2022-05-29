import flask
app = flask.Flask(__name__)
@app.route('/hello',methods = ["GET","POST"])
def hello_world():
    if flask.request.method == "GET":
        return flask.render_template("form.html")
    elif flask.request.method == "POST":
        name = flask.request.form["name"]
        return flask.render_template("display.html",name = name)
if __name__=="__main__":
    app.debug = True
    app.run()