#!flask/bin/python
from flask import Flask,request,render_template,jsonify
import lib.link_test as validate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def index_post():
    try:
        url = request.form['search']
        data = validate.test_links(url)
        keys = ['URL','Code']
        return render_template("index.html", data=data, keys=keys)
    except requests.exceptions.MissingSchema:
        return "Error. Please Use Full URL (e.g \"https://google.com\")"

@app.route('/api',methods = ['GET','POST'])
def api():
    if request.method !='POST':
        return "Only POST allowed."
    data = request.get_data()
    return jsonify(validate.test_links(data))

if __name__ == '__main__':
    app.run(host='0.0.0.0')
