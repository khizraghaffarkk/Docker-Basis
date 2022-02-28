import csv
import time
import logging
import os
from itertools import islice
import paho.mqtt.client as mqtt

BROKER_URL = os.environ['MQTT_URL']
BROKER_PORT = 1883
CLIENT_ID = "student012"

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
                        #logging.debug("Signal \t" + signals_list[i] + "\n")
                        #logging.debug("Value \t " + row[i] + " " + units_list[i] + "\n")
                        #print("Signal \t" + signals_list[i] + "\n")
                        #print("Value \t " + row[i] + " " + units_list[i] + "\n")
                        result = client.publish(topic="toyota/" + signals_list[i], payload=row[i], qos=0, retain=False)
                        print(result)
                        
                time.sleep(0.001)
                #time.sleep(delta)

                prev_time = curr_time

def main():
    #log_level = getattr(logging, loglevel.upper(), None)
    #logging.basicConfig(level=log_level)
    
    client = mqtt.Client()
    client.connect(BROKER_URL, BROKER_PORT) 
    readData(client)

 


if __name__ == "__main__":
    main()
