import paho.mqtt.client as mqtt
import time

host="node02.myqtthub.com"  #MQTT server address
port=1883  #MQTT server port
clean_session=True
client_id="pythonPub"  #client ID
username="pilogin"  #client username
password="ph5yVnQ1-kOOdGRoj"  #client password
topic="heatingsystem"  #topic
# message="message from Python client"

#call-back function on connection
def on_connect(client,userdata,flags,rc):
    print("Connect {} result is: {}".format(host,rc))
    if rc==0:
        client.connected_flag=True
        print("connected ok")
        return
    print("Failed to connect {}, error was, rc={}".format(host,rc))
    
#run to publish
def run(roomname,temperature):

    fullmessage = (roomname + "-" + str(temperature))
    print("This is the full message " + fullmessage)

    client=mqtt.Client(client_id=client_id,clean_session=clean_session)
    client.on_connect=on_connect
    client.username_pw_set(username,password)  #set username and password
    client.connect(host,port,keepalive=60)  #try to connect
    client.connected_flag=False
    
    #loop until connected
    while not client.connected_flag:
        client.loop()
        time.sleep(1)
        
    ret=client.publish(topic,fullmessage)  #publish message
    print("Publish result: {}".format(ret.rc))
    client.disconnect()  #disconnect
    
if __name__=="__main__":
    run()