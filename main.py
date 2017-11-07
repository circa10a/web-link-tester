#!flask/bin/python
from flask import Flask,request,render_template,jsonify
import lib.link_test as validate

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
        url = request.form['search']
        data = validate.test_links(url)
        if isinstance(data, list):
            keys = ['URL','Code']
            return render_template('index.html', data=data, keys=keys)
        else:
            return render_template('index.html', invalid_data=data)

@app.route('/api',methods = ['GET','POST'])
def api():
    if request.method !='POST':
        return 'Only POST allowed.'
    data = validate.test_links(request.get_data())
    if isinstance(data, list):
        return jsonify({'links': data})
    else:
        return data

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
