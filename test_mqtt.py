import paho.mqtt.client as mqtt
import time

connection_topic = "CLIENT_CONNECTED"
def on_connect(client, userdata, flags, rc):
    #0: Connection successful
    #1: Connection refused – incorrect protocol version
    #2: Connection refused – invalid client identifier
    #3: Connection refused – server unavailable
    #4: Connection refused – bad username or password
    #5: Connection refused – not authorised
    #6-255: Currently unused.
    if rc==0:
        print('connecting')
        client.connected_flag=True
        client.publish(connection_topic,1,retain=True)
    else:
        client.bad_connection_flag=True

def on_disconnect(client, userdata, rc):
    print('disconnecting')
    client.connected_flag=False
    client.disconnect_flag=True

def on_message(client, userdata, msg):
    print(msg.topic + ' ' + str(msg.payload))

def on_log(client, userdata, level, buf):
    print("log: ",buf)




client = mqtt.Client("C1")

client.connected_flag=False
client.on_connect = on_connect
client.on_disconnect = on_disconnect
client.on_log = on_log
client.on_message = on_message
#client.on_unsubscribe=client.on_unsubscribe ##  on_unsubscribe(client, userdata, mid)  unsubscribe(topic)

client.loop_start()
client.connect("0.0.0.0", 1883, 60)


while not client.connected_flag: #wait in loop
    print("In wait loop")
    time.sleep(1)


client.subscribe("go_to_left")

#client.loop_forever()
while True:
        time.sleep(1)
        client.loop()


client.loop_stop()
