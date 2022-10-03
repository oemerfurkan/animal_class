from email.mime import base
from flask import Blueprint, render_template, request, flash
import pymongo

client = pymongo.MongoClient("mongodb+srv://oemerfurkan:123321@cluster0.ocu6zjv.mongodb.net/?retryWrites=true&w=majority")
db = client.animals
collection = db.animal_classes

views = Blueprint('views', __name__)

@views.route('/', methods=["GET", "POST"])
def home():
    if request.method == "POST":
        animal_class = request.form.get("animal_class")
        token = request.form.get("token")

        if collection.find_one({"animal_class" : f"{animal_class}"}) == None or collection.find_one({"token" : f"{token}"}) == None:
            return render_template("error.html")
        else:
            flash(collection.find_one({"token" : f"{token}", "animal_class" : f"{animal_class}" })["animals"])
    return render_template("base.html")