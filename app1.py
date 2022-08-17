from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def homepage():
    return 'Hello World!'

@app.route('/sec')
def secondpage():
    return '<h1> Hello </h1>'

@app.route('/third/<name>')
def printname(name):
    return 'Hello ' + name

@app.route('/add/<a>/<b>')
def add_num(a,b):
    return str(int(a) + int(b))

@app.route('/add1/<li>')
def add_list(li):
    kap_sum = 0
    li = li.split(',')
    for i in li:
        kap_sum += float(i)
    return str(kap_sum)

@app.route('/log_trial/<id>,<pwd>')
def log_trial(id,pwd):
    if id == 'admin' and pwd == '123':
        return 'Hello ' + id
    else:
        return 'Wrong password'

@app.route('/json_trial', methods = ['POST'])
def json_trial():
    if request.method == 'POST':
        # print(request.json)
        a = request.json['num1']
        b = request.json['num2']
        res = a + b
    return str(res)

@app.route('/json_login_trial', methods = ['POST'])
def json_login_trial():
    if request.method == 'POST':
        a = request.json
        if a['id'] == 'admin' and a['pwd'] == 123:
            return jsonify(f"Hello {a['id']}")

@app.route('/json_login_trial2', methods = ['GET'])
def json_login_trial2():
    if request.method == 'GET':
        a = request.json
        try:
            if a['id'] == 'admin' and a['pwd'] == 123:
                return jsonify(f"Hello {a['id']}")
        except Exception as e:
            print('Exception ',e)
            return jsonify(str(e))


if __name__ == '__main__':
    app.run(debug=True)