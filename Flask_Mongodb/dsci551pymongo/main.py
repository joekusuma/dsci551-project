from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
from flask import Blueprint, render_template

dsci551db = MongoClient(
    "mongodb+srv://dsci551:w8QBPtSfunya7Gy0@clusterdsci551.s85edni.mongodb.net/?retryWrites=true&w=majority"
)

main = Blueprint("main", __name__)

polls = [
    {
        "id": 1,
        "title": "What is your favorite color?",
        "description": "Choose one of the following colors.",
        "options": ["Red", "Green", "Blue"],
        "votes": [3, 2, 1],
    },
    {
        "id": 2,
        "title": "What is your favorite food?",
        "description": "Choose one of the following foods.",
        "options": ["Pizza", "Burgers", "Tacos"],
        "votes": [5, 3, 2],
    },
    {
        "id": 3,
        "title": "What is your favorite movie?",
        "description": "Choose one of the following movies.",
        "options": ["Star Wars", "The Godfather", "The Shawshank Redemption"],
        "votes": [1, 4, 5],
    },
]

new_poll = []


@main.route("/")
def index():
    # user_collection = dsci551db.dsci551.users
    # user_collection.insert_one({"name": "Tiger", "age": 24})
    # user_collection.insert_one({"name": "Joe", "age": 22})
    return render_template("index.html")


@main.route("/find")
def find():
    # user_collection = dsci551db.dsci551.users
    # user = user_collection.find_one({"name": "Tiger"})
    return render_template("index.html", user=user)


@main.route("/update")
def update():
    # user_collection = dsci551db.dsci551.users
    # filter = {"name": "Tiger"}
    # newvalues = {"$set": {"age": 80}}
    # user_collection.update_one(filter, newvalues)
    return render_template("index.html")


@main.route("/delete")
def delete():
    # user_collection = dsci551db.dsci551.users
    # filter = {"name": "Tiger"}
    # user_collection.delete_one(filter)
    return render_template("index.html")


@main.route("/create-poll", methods=["GET", "POST"])
def create_poll():
    if request.method == "POST":
        title = request.form["title"]
        description = request.form["description"]
        options = request.form["options"]
        # votes = request.form["votes"]
        new_poll.append(
            {
                "title": title,
                "description": description,
                "options": list(options.split(",")),
                # "votes": votes,
            }
        )
        poll_collection = dsci551db.dsci551.polls
        poll_collection.insert_many(new_poll)
        return redirect(url_for("main.view_polls"))
    return render_template("create_poll.html")


@main.route("/view-polls")
def view_polls():
    poll_collection = dsci551db.dsci551.polls
    for x in poll_collection.find():
        new_poll.append(x)
    return render_template("view_polls.html", polls=new_poll)


# @main.route("/vote")
# def vote():

#     return render_template("vote.html", polls=polls)


@main.route("/login")
def login():
    return render_template("login.html")


app = Flask(__name__)
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)
