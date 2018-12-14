from picamera import PiCamera
from time import sleep
import cv2
from datetime import datetime

x=datetime.now().strftime("%H_%M_%S")+".jpg"
camera = PiCamera()

#カメラが画像の取得を開する
camera.start_preview()

#// 5秒待つ
sleep(3)

#// 画像を収録して保存
camera.capture('/home/pi/data/jpgdir/'+x)

#// カメラが画像の取得を停止する
camera.stop_preview()
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 95]
img = cv2.imread('/home/pi/data/jpgdir/'+x)
result, encimg = cv2.imencode('.jpg', img, encode_param)
decimg = cv2.imdecode(encimg,1)
cv2.imwrite('test12.jpg', decimg)


