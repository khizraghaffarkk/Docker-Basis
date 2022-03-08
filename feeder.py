import csv
import time
import logging
import os
from itertools import islice
import paho.mqtt.client as mqtt

BROKER_URL = os.environ['MQTT_URL']
BROKER_PORT = os.environ['MQTT_PORT']
CLIENT_ID = os.environ['CLIENT_ID']
is_connected = False

def readData(client):
    with open("toyota_data.csv", "r", newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='"')
        
        signals_list = next(reader)
        units_list = next(reader)
        while True:
            csvfile.seek(0)
            prev_time = 0
            for row in islice(reader, 2, None):

                curr_time = float(row[0])

                if prev_time != 0:
                    delta = (curr_time-prev_time)
                else:
                    delta = 0

                for i in range (1,46):

                    if row[i] != "":
                        client.publish(topic= CLIENT_ID + "/toyota/" + signals_list[i], payload=row[i], qos=0, retain=False)
                        
                time.sleep(delta)

                prev_time = curr_time

def main():
    
    client = mqtt.Client()
    client.tls_set("ca.crt")
    client.tls_insecure_set(True)
    client.on_connect = on_connect
    client.on_publish = on_publish
    client.connect(BROKER_URL, int(BROKER_PORT))
    client.loop_start()
    
    while is_connected != True:
        
        print("Connecting...")
        time.sleep(5)
    readData(client)

    client.loop_stop()
    client.disconnect()
def on_connect(client, userdata, flags, rc):
    if rc==0:
        global is_connected
        is_connected = True
        print("Connected to broker")
    else:
        is_connected = False
        print("Failed to connected with result " + str(rc))

def on_disconnect(client, userdata, rc):
    if rc != 0:
        print("Unexpected disconnection.")

def on_publish(client, userdata, result):
        print("Msg id published: "+ str(result))
    

if __name__ == "__main__":
    main()
