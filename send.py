from picamera import PiCamera
from time import sleep
from datetime import datetime
import cv2
filename=datetime.now().strftime("%H_%M_%S")+".jpg"
camera = PiCamera()

#カメラが画像の取得を開する
camera.start_preview()

#// 5秒待つ
sleep(2)
img_file = '/home/pi/data/jpgdir/'+filename
#// 画像を収録して保存
camera.capture(img_file)

#// カメラが画像の取得を停止する
camera.stop_preview()
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 50]
img = cv2.imread( img_file )
result, encimg = cv2.imencode('.jpg', img, encode_param)
decimg = cv2.imdecode(encimg,1)
cv2.imwrite(img_file, decimg)





import urllib.request
import urllib.parse #URLエンコード
import base64

b64 = base64.encodestring(open(img_file, 'rb').read())

#url = input()
#url = ""

data = {"data":b64 , "filename":filename} #Form data
encd_prm = urllib.parse.urlencode(data).encode("utf-8") #パラメータ(data)をURLエンコード
url = "http://ik1-334-27288.vs.sakura.ne.jp/sotuken/get_ras.php"
#リクエスト送信・レスポンス受信
with urllib.request.urlopen(url, data=encd_prm) as response: #POSTメソッドでデータを送信するには，第二
    html = response.read().decode("utf-8")
    print(html)

