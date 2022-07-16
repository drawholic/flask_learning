from flask import Flask, request, make_response
from db_setup import create_user, log_user

app = Flask(__name__)


@app.route('/')
def index():
    meth = request.cookies.get('user')
    return f'<p>Hello world</p> {request.path}, {meth}'


@app.route('/user/create', methods=[ 'POST'])
def register():

        username = request.json['username']
        password = request.json['password']
        try:
            if create_user(username, password):
                res = make_response({'status':200, 'text':'created'})
                return res
            else:
                res = make_response({'status':400, 'text': 'user with that username already exists'})
                return res
        except Exception as e:
            print(e)
            res = make_response({'status':400})
            return res


@app.route('/user/login/', methods=['POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    if log_user(username, hash(password)):
        res = make_response({'status':200, 'text':'logged'})
        return res
    else:
        res = make_response({'status':400, 'text':'you have to be registered to log'})
        return res