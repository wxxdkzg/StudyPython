#RECRIVING Client

import paho.mqtt.client as mqtt

broker_url = "127.0.0.1"
broker_port = 1883

def on_connect(client, userdata, flags, rc):
   print("Connected With Result Code " (rc))

def on_disconnect(client, userdata, rc):
   print("DisConnected With Result Code " (rc))

def on_message_from_kitchen(client, userdata, message):
   print("Message Recieved from Kitchen: "+message.payload.decode())

def on_message_from_bedroom(client, userdata, message):
   print("Message Recieved from bedroom: "+message.payload.decode())

def on_message_TestingTopic(client, userdata, message):
   print("Message Recieved from TestingTopic: "+message.payload.decode())

def on_message(client, userdata, message):
   print("Message Recieved from Others: "+message.payload.decode())

client = mqtt.Client()
client.connect(broker_url, broker_port)
client.on_connect = on_connect
client.on_disconnect = on_disconnect
#To Process Every Other Message
client.on_message = on_message


client.subscribe("TestingTopic", qos=1)
client.subscribe("KitchenTopic", qos=1)
client.subscribe("BedroomTopic", qos=1)
client.message_callback_add("TestingTopic", on_message_TestingTopic)
client.message_callback_add("KitchenTopic", on_message_from_kitchen)
client.message_callback_add("BedroomTopic", on_message_from_bedroom)

client.loop_forever()