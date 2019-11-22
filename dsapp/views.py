from flask import Flask, render_template, jsonify, Response
from random import *
from flask_cors import CORS
import time

app = Flask(__name__)

# Config options - Make sure you created a 'config.py' file.
app.config.from_object('config')
# To get one variable, tape app.config['MY_VARIABLE']

# enable CORS (Cross origin resource sharing) ==> 
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
# !!! ATTENTION !!! here it allows all origins. Sanitize for prod mode !!!!!!
# !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
CORS(app, resources={r'/*': {'origins': '*'}})

def get_message():
  '''this could be any function that blocks until data is ready'''
  time.sleep(1.0)
  s = time.ctime(time.time())
  return s


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/data')
def data():
    x = [1, 2, 3, 4, 5]
    y = [randint(1,20), randint(1,20), randint(1,20), randint(1,20), randint(1,20)]
    
    return jsonify(x=x, y=y)

@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

# This is SSE part
@app.route('/stream')
def stream():
    def eventStream():
        while True:
            # wait for source data to be available, then push it
            yield 'data: {}\n\n'.format(get_message())
    return Response(eventStream(), mimetype="text/event-stream")

if __name__ == "__main__":
    app.run()