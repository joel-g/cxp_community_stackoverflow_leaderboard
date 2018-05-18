from flask import Flask, render_template
import requests

app = Flask(__name__)

STACK_IDS=('8826629', '9541448', '6591675', '7452904', '9393813', '8840926')

def get_user(user_id):
    res = requests.get("http://api.stackexchange.com/2.2/users/" + user_id + "?order=desc&sort=reputation&site=stackoverflow")
    return res.json()['items'][0]

@app.route('/')
def index(users=None):
    jsons = []
    for user_id in STACK_IDS:
        jsons.append(get_user(user_id))
    jsons = sorted(jsons, key=lambda k: k['reputation_change_week'], reverse=True)
    return render_template('index.html', users=jsons)