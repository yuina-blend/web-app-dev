#　南義貴

# モジュールのインポート
from flask import Flask,render_template,request
import cv2
from .GenerateTextImage import GenerateTextImage
app=Flask(__name__)

#　最初の表示
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

#　変更後の表示
#　入力した情報を保持して画像を出力
@app.route('/index',methods=['post'])
def post():
    text=request.form.get('text')
    font=request.form.get('font')
    color=request.form.get('color')
    textsize=request.form.get('textsize')
    height=request.form.get('height')
    width=request.form.get('width')

    #OpenCVフォントの辞書
    cv2fonts = {
        'simplex':cv2.FONT_HERSHEY_SIMPLEX,
        'plain':cv2.FONT_HERSHEY_PLAIN,
        'duplex':cv2.FONT_HERSHEY_DUPLEX,
        'complex':cv2.FONT_HERSHEY_COMPLEX,
        'triplex':cv2.FONT_HERSHEY_TRIPLEX,
        'complex_small':cv2.FONT_HERSHEY_COMPLEX_SMALL,
        'script_simplex':cv2.FONT_HERSHEY_SCRIPT_SIMPLEX,
        'script_complex':cv2.FONT_HERSHEY_SCRIPT_COMPLEX,
        'italic':cv2.FONT_ITALIC
    }
    # カラーコードをRGB値タプルに変換
    rgb=(int(color[1:3], 16), int(color[3:5], 16), int(color[5:7], 16))
    # 画像生成
    textimg = GenerateTextImage()
    textimg.generate(int(height), int(width), (255, 255, 255), text, rgb, cv2fonts.get(font), float(textsize))

    return render_template('index.html')

