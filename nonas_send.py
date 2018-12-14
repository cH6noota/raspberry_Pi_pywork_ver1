from picamera import PiCamera
from time import sleep
from datetime import datetime
import cv2
filename=datetime.now().strftime("%H_%M_%S")+".jpg"
camera = PiCamera()

camera.start_preview()

sleep(2)
img_file = '/home/pi/data/jpgdir/'+filename
camera.capture(img_file)

camera.stop_preview()
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 50]
img = cv2.imread( img_file )
result, encimg = cv2.imencode('.jpg', img, encode_param)
decimg = cv2.imdecode(encimg,1)
cv2.imwrite(img_file, decimg)





import urllib.request
import urllib.parse
import base64

b64 = base64.encodestring(open(img_file, 'rb').read())


data = {"data":b64 , "filename":filename} #Form data
encd_prm = urllib.parse.urlencode(data).encode("utf-8") 
url = "http://ik1-334-27288.vs.sakura.ne.jp/sotuken/get_ras.php"
with urllib.request.urlopen(url, data=encd_prm) as response: 
    html = response.read().decode("utf-8")
    print(html)

