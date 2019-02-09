#Flask imports
from flask import Flask, jsonify, request
app = Flask(__name__)


import pickledb

db = pickledb.load('FEEB.db', False)

@app.route('/')
def hello_world():
    return 'Hello, World!'

#Getting and posting json
# import requests
# res = requests.post('http://localhost:5000/api/add_message/1234', json={"mytext":"lalala"})
# if res.ok:
#     print res.json()

# from flask import Flask, request, jsonify
# app = Flask(__name__)

@app.route('/api/add_schedule/<schedule_id>', methods=['GET', 'POST'])
def add_schedule(schedule_id):
    if request.method == 'POST':
        content = request.json
        db.set('schedule_{}'.format(schedule_id), content)
        return jsonify({"sid":schedule_id})
    else:
        content = db.get('schedule_{}'.format(schedule_id))
        return jsonify(content)




#Get and post at the same time:
# def register():
#     if flask.request.method == 'POST':
#         username = flask.request.values.get('user') # Your form's
#         password = flask.request.values.get('pass') # input names
#         your_register_routine(username, password)
#     else:
#         # You probably don't have args at this route with GET
#         # method, but if you do, you can access them like so:
#         yourarg = flask.request.args.get('argname')
#         your_register_template_rendering(yourarg)


if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=True)