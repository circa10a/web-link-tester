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
    data = request.get_data()
    return jsonify(validate.test_links(data))

if __name__ == '__main__':
    try:
        app.run(host='0.0.0.0',port=5000)
    except KeyboardInterrupt:
        print('Aborted')
