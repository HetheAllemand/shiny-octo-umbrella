from flask import FLASK

app = Flask(__name__)


@app.get("/")
def about_me():
    me = {
        "first_name": "Hethe",
        "last_name": "Allemand",
        "hobbies": "golf", 
        "active": True
    }

    return me