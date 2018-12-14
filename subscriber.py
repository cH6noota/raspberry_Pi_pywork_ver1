import paho.mqtt.client as mqtt

host = '153.126.197.42'
port = 1883
topic = 'topicA'

def on_connect(client, userdata, flags, respons_code):
    print(topic+"としてMQTTスタート")
    client.subscribe(topic)

def on_message(client, userdata, msg):
    x=(msg.payload).decode('utf-8')
    print(msg.topic + ' ' + x)

if __name__ == '__main__':

    # Publisherと同様に v3.1.1を利用
    client = mqtt.Client(protocol=mqtt.MQTTv311)

    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(host, port=port, keepalive=60)

    # 待ち受け状態にする
    client.loop_forever()
