from flask import Flask
from flask import render_template
from flask import make_response

app = Flask(__name__)

@app.route('/')
def index():
    resp = make_response(render_template('index.html'))
    resp.set_cookie('cereal', 'GCTF{HUNG7Y_L177L3_B01}')
    return resp

if __name__ == '__main__':
    app.run()
