from flask import Flask, render_template
import requests

app = Flask(__name__)

STACK_IDS=('8826629','9541448', '6591675', '7452904', '9393813', '8840926', '9454112', '7287446', '9598801', '9541439', '9554961', '8797362', '8748848', '9672092', '9603809', '9536851', '8366814', '9541510', '9541342', '8826629')

def get_user(user_id):
    res = requests.get("http://api.stackexchange.com/2.2/users/" + user_id + "?order=desc&sort=reputation&site=stackoverflow&key=dS6SG)8rCYRWj0DcXzmJ4w((")
    return res.json()['items'][0]
    # Don't steal my API key. Just get your own free one.

def rank_users(order_by):
    jsons = map(get_user, STACK_IDS)
    jsons = sorted(jsons, key=lambda k: k[order_by], reverse=True)
    return jsons

@app.route('/')
def index(users=None):
    jsons = rank_users("reputation")
    return render_template('index.html', users=jsons, title="Total Reputation")

@app.route('/week')
def total(users=None):
    jsons = rank_users("reputation_change_week")
    return render_template('index.html', users=jsons, title="Rep Change this Week") 

@app.route('/month')
def month(users=None):
    jsons = rank_users("reputation_change_month")
    return render_template('index.html', users=jsons, title="Rep Change this Month")

if __name__ == '__main__':
    app.run()
