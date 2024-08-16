from flask import Flask, request, render_template, redirect, make_response

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("base.html")


@app.route("/welcome", methods=["POST"])
def welcome():
    name = request.form["name"]
    email = request.form["email"]

    resp = make_response(redirect("/hello"))
    resp.set_cookie("user_name", name)
    resp.set_cookie("user_email", email)
    return resp


@app.route("/hello")
def hello():

    user_name = request.cookies.get("user_name")
    if user_name:
        return render_template("hello_2.html", name=user_name)
    return redirect("/")


@app.route("/logout")
def logout():
    resp = make_response(redirect("/"))
    resp.delete_cookie("user_name")
    resp.delete_cookie("user_email")
    return resp


if __name__ == "__main__":
    app.run(debug=True)
