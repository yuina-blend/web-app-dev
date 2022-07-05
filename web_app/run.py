#　南義貴

# モジュールのインポート
from flask import Flask,render_template,request
app=Flask(__name__)

#　最初の表示
@app.route('/')
def index():
    return render_template('index.html')

#　変更後の表示
#　入力した情報を保持して画像を出力
@app.route('/index',methods=['post'])
def post():
    text=request.form.get['text']
    font=request.form.get['font']
    color=request.form.get['color']
    charsize=request.form.get['charsize']
    imgsize=request.form.get['imgsize']
    return render_template(
        'index.html',text=text,font=font,color=color,
        charsize=charsize,imgsize=imgsize)

if __name__=='__main__':
    app.debug=True
    app.run(host='localhost')
