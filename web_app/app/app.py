#　南義貴

# モジュールとファイルのインポート
from flask import Flask,render_template,request
import GenerateTextImage

app=Flask(__name__)

#　最初の表示
@app.route('/')
def index():
    return render_template('index.html')

#　変更後の表示
#　入力した情報を保持して画像を出力
@app.route('/index',methods=["post"])
def post():
    text=request.form['text']
    font=request.form['font']
    color=request.form['color']
    charsize=request.form['charsize']
    imgsize=request.form['imgsize']

    generate=generate()
    backcolor=(imgsize,imgsize,3)
    generate.generate(
        generate,imgsize,imgsize,backcolor,text,color,font,charsize)

    return render_template(
        'index.html',text=text,font=font,color=color,
        charsize=charsize,imgsize=imgsize)

if __name__=='__main__':
    app.run(debug=True)
