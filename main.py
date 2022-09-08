from flask import Flask, render_template, redirect, request
from replit import db
import random, string
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

app = Flask('app')
shortener_page = 'https://safeds.tk/u/'
port = random.randint(10000, 40000)

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["50 per minute", "1 per second"],
)

key = ''
for i in range(10) : key += random.choice(string.ascii_lowercase)
app.config["SECRET_KEY"] = key

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/test')
def test():
  return render_template('example.html')

@app.route('/u/<shorten>')
@limiter.exempt
def linking(shorten):
  value = db[shorten]
  return redirect(value)

@app.route('/api', methods = ["GET", "POST"])
@limiter.exempt
def api():
  print(request.args.get('link', type = str))
  result = ""
  for i in range(4) :
      result += random.choice(string.ascii_lowercase)
  db[result] = request.args.get('link', type = str)
  return render_template('result.html', url=f"{shortener_page}{result}")

app.run(host='0.0.0.0', port=port, debug = True)