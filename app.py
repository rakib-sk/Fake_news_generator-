from flask import Flask, request, render_template
import random
import json
from flask_frozen import Freezer

app = Flask(__name__)

with open("news_data.json", "r", encoding="utf-8") as f:
    data = json.load(f)

actions = data["actions"]
places = data["places"]

@app.route("/", methods=["GET", "POST"])
def fake_news():
    if request.method == "POST":
        person_name = request.form.get("person_name", "").strip()

        if not person_name:
            return render_template("index.html", headline="Please enter a person name")

        subject = person_name
        action = random.choice(actions)
        place = random.choice(places)

        headline = f"{subject} {action} {place}!"

        return render_template("index.html", headline=headline)

    return render_template("index.html")


# Frozen-Flask
freezer = Freezer(app)

if __name__ == "__main__":
    
    freezer.freeze()