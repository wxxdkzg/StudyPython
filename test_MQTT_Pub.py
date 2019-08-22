#Publishing Client

import paho.mqtt.client as mqtt

broker_url = "127.0.0.1"
broker_port = 1883


def on_connect(client, userdata, flags, rc):
    print("Connected With Result Code "(rc))


def on_disconnect(client, userdata,  rc):
    print("DisConnected With Result Code "(rc))


client = mqtt.Client()
client.connect(broker_url, broker_port)
client.on_connect = on_connect
client.on_disconnect = on_disconnect

client.publish(topic="KitchenTopic", payload="KitchenTopic,TestingPayload", qos=1, retain=False)
client.publish(topic="TestingTopic", payload="TestingTopic,TestingPayload", qos=1, retain=False)
client.publish(topic="BedroomTopic", payload="BedroomTopic,TestingPayload", qos=1, retain=False)