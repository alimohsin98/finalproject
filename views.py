from flask import Flask, render_template, Blueprint, url_for,redirect
my_view= Blueprint('my_view', __name__)

@my_view.route("/")
@my_view.route("/index")
def index():
    return render_template("index.html")

@my_view.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@my_view.route("/phones")
def phones():
    return render_template("phones.html")

@my_view.route("/pcs")
def pcs():
    return render_template("pcs.html")

@my_view.route("/tvs")
def tvs():
    return render_template("tvs.html")

@my_view.route("/consoles")
def consoles():
    return render_template("consoles.html")

