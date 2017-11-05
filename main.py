#!flask/bin/python
from flask import Flask,request,render_template,jsonify
import json
import lib.link_test as validate

app = Flask(__name__)
def removew(d):
  for k, v in d.iteritems():
    if isinstance(v, dict):
      removew(v)
    else:
      d[k]=v.strip()

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def index_post():
    url = request.form['search']
    data = validate.test_links(url)
    data = removew(data)
    keys = ['url','code']
    return render_template("index.html", data=data, keys=keys)

@app.route('/api',methods = ['GET','POST'])
def api():
    if request.method !='POST':
        return "Only POST allowed."
    data = request.get_data()
    return jsonify(validate.test_links(data))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
