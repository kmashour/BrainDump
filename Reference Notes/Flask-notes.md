---
tags:
  - flask
Type: Reference Note
source: udemy.com/course/web-developer-bootcamp-flask-python
page:
links:
---
export FLASK_APP=app.py
export FLASK_ENV=DEBUG

# Flask App Factory pattern 
Very important because in deployments we may end up running multiple mongo clients this help us avoid that in addition

All `create_app()` helps us to running this function from my test and passing different parameters 


```
import datetime

from flask import Flask, render_template, request

from pymongo import MongoClient

  

def create_app():

    app = Flask(__name__)

	client = MongoClient("mongodb+srv://karimkimo991km_db_user:aKeqRMzcJoLcasUz@cluster0.ddabtkh.mongodb.net/")

    app.db = client.microblog

  

    @app.route("/", methods=["GET", "POST"])

    def home():

        # entries = []

        if request.method == "POST":

            entry_content = request.form.get("content")

            formatted_date = datetime.datetime.today().strftime("%Y-%m-%d")

            print(f"Received new entry: {entry_content} on {formatted_date}")

            # entries.append({"content": entry_content, "date": formatted_date})

  

            #inserted one document into the entries collection

            app.db.entries.insert_one({"content": entry_content, "date": formatted_date})

        entries_with_date = [

            (

                entry["content"],

                entry["date"],

                datetime.datetime.strptime(entry["date"], "%Y-%m-%d").strftime("%b %d")

            )

            for entry in app.db.entries.find()

            #for entry in app.db.entries.find({}), {} state no filters no restrictions                matters all documents

        ]

        return render_template("home.html", entries=entries_with_date)

    return app
```



# Flask Redirection scenarios 












