
#coding: utf-8
import urllib.request
import urllib.parse #URLエンコード
import base64

img_file = '/home/pi/data/jpgdir/14_59_02.jpg'
b64 = base64.encodestring(open(img_file, 'rb').read())

#url = input()
#url = ""

print("post.php")
data = {"data":b64 , "filename":"test.jpg"} #Form data
encd_prm = urllib.parse.urlencode(data).encode("utf-8") #パラメータ(data)をURLエンコード
url = "http://ik1-334-27288.vs.sakura.ne.jp/sotuken/get_ras.php"
#リクエスト送信・レスポンス受信
with urllib.request.urlopen(url, data=encd_prm) as response: #POSTメソッドでデータを送信するには，第二引数にエンコードしたデータを入れてやる．
    html = response.read().decode("utf-8")
    print(html)
