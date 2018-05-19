from flask import Flask, render_template
import requests

app = Flask(__name__)

STACK_IDS=('8826629','9541448', '6591675', '7452904', '9393813', '8840926', '9454112', '7287446', '9598801', )

def get_user(user_id):
    res = requests.get("http://api.stackexchange.com/2.2/users/" + user_id + "?order=desc&sort=reputation&site=stackoverflow")
    return res.json()['items'][0]

def pagify_users(order_by):
    jsons = []
    for user_id in STACK_IDS:
        jsons.append(get_user(user_id))
    jsons = sorted(jsons, key=lambda k: k[order_by], reverse=True)
    return jsons

@app.route('/')
def index(users=None):
    jsons = pagify_users("reputation_change_week")
    return render_template('index.html', users=jsons, title="Rep Change this Week")

@app.route('/total')
def total(users=None):
    jsons = pagify_users("reputation")
    return render_template('index.html', users=jsons, title="Total Reputation")

@app.route('/month')
def month(users=None):
    jsons = pagify_users("reputation_change_month")
    return render_template('index.html', users=jsons, title="Rep Change this Month")