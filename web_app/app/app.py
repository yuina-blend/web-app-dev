# モジュールとファイルのインポート
from flask import Flask,render_template,request
import cv2
import base64

# run.pyで連携するとき
from app.GenerateTextImage import GenerateTextImage

# app.pyから実行するとき
#from .GenerateTextImage import GenerateTextImage

app=Flask(__name__)

#　最初の表示
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

#　変更後の表示
@app.route('/index',methods=['post'])
def post():

    # 入力したデータを取得
    text=request.form['text']
    font=request.form['font']
    color=request.form['color']
    textsize=request.form['textsize']
    height=request.form['height']
    width=request.form['width']

    # インスタンス生成
    generate=GenerateTextImage()

    # 背景色を白にする（白はRGB=(255,255,255)）
    backcolor=(255,255,255)

    # フォントの確認
    # OpenCVのフォント指定を辞書型で定義
    fonttype={
        "simplex":cv2.FONT_HERSHEY_SIMPLEX,
        "plain":cv2.FONT_HERSHEY_PLAIN,
        "duplex":cv2.FONT_HERSHEY_DUPLEX,
        "complex":cv2.FONT_HERSHEY_COMPLEX,
        "triplex":cv2.FONT_HERSHEY_TRIPLEX,
        "complex_small":cv2.FONT_HERSHEY_COMPLEX_SMALL,
        "script_simplex":cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
        "script_complex":cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
        "italic":cv2.FONT_ITALIC
    }
    # フォントを指定
    for i in fonttype.keys():
        if i == font:
            font=fonttype[i]
    
    # テキストの色を指定 
    color=(int(color[5:7],16),int(color[3:5],16),int(color[1:3],16))

    # 画像を生成
    img_base64 = generate.generate(
        int(height),int(width),backcolor,text,color,font,int(textsize))

    # HTMLを返す
    return render_template('index.html', img_base64=img_base64)

if __name__=='__main__':
    app.debug=True
    app.run(host='localhost')
