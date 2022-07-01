from flask import Flask,render_template,request
app=Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/',methods=['post'])
def post():
    name=request.form['name']
    return render_template('index.html',name=name)

if __name__=='__main__':
    app.debug=True
    app.run(host='localhost')
