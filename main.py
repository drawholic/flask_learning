from flask import Flask, request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    meth = request.cookies.get('user')
    return f'<p>Hello world</p> {request.path}, {meth}'


@app.route('/user', methods=['GET', 'POST'])
def user():
    res = make_response('here is a response <form method="post"><input type="submit"/></form>')
    req = request.method
    if request.method == 'GET':
        return res
    else:
        return req