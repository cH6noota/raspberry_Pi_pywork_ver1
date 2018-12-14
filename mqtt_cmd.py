import paho.mqtt.client as mqtt
import subprocess
host = '153.126.197.42'
port = 1883
topic = 'topicA'

def on_connect(client, userdata, flags, respons_code):
    print(topic+"としてMQTTスタート")
    client.subscribe(topic)

def on_message(client, userdata, msg):
    pub_client = mqtt.Client(protocol=mqtt.MQTTv311)
    pub_client.connect(host, port=port, keepalive=60)
    x=(msg.payload).decode('utf-8')
    cmdlist=x.split("_")
    print(msg.topic + ' ' + x)
    if(x=="チョコレート"):
        try:
                print("Hi,チョコレート！")
                res = subprocess.check_output('python3 /home/pi/pywork/send.py ' ,shell=True)
                pub_client.publish(topic, res)
                pub_client.disconnect()
        except:
                print ("Error")
                pub_client.publish(topic, 'エラーが出たよぉぉ')
                pub_client.disconnect()
    elif(cmdlist[0]=="実行"):
        try:
                print("赤外線実行する")
                res ="OK"
          
                subprocess.check_output('irsend  SEND_ONCE pc_room_light '+cmdlist[1] ,shell=True)
                pub_client.publish(topic, res)
                pub_client.disconnect()
        except:
                print ("Error")
                pub_client.publish(topic, 'エラーが出たよぉぉ')
                pub_client.disconnect()

if __name__ == '__main__':
    # Publisherと同様に v3.1.1を利用
    client = mqtt.Client(protocol=mqtt.MQTTv311)

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(host, port=port, keepalive=60)

    # 待ち受け状態にする
    client.loop_forever()
