from flask import Flask, render_template, redirect, request
from replit import db
import random, string

app = Flask('app')
shortener_page = 'https://sher.kro.kr/u/'
port = int('3410')

key = ''
for i in range(10) : key += random.choice(string.ascii_lowercase)
app.config["SECRET_KEY"] = key

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/u/<shorten>')
def linking(shorten):
  value = db[shorten]
  return redirect(value)

@app.route('/api', methods = ["GET", "POST"])
def api():
  print(request.args.get('link', type = str))
  result = ""
  for i in range(4) :
      result += random.choice(string.ascii_lowercase)
  db[result] = request.args.get('link', type = str)
  return render_template('result.html', url=f"{shortener_page}{result}")

app.run(host='0.0.0.0', port=port, debug=True)