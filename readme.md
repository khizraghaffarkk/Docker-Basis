# Toyota-data-feeder

This is a demo application which playbacks included .csv file indefinitely, and sends it as mqtt message to mqtt broker.
Included csv contains raw data dump with mapped signals and units of Toyota RAV4 Hybrid car.

Do note that for the first 5 minutes there is not much happening. This is because the driver of the car was doing something else than driving. Log file takes 13 minutes to playback.

## Dev environment

Python 3.9

It is recommended to setup Python virtualenv first

```
python3 -m venv .venv
source .venv/bin/Activate
pip install -r requirements.txt
```
## MQTT Broker

This application requires an MQTT broker which is set up in a CSC Rahti cloud with correct certificates. 

Application uses included ca.crt for establishing encrypted connection but doesn't check for server hostname.
## Environment variables

Application takes three env variables

- `MQTT_URL`
    Takes Mqtt broker url
- `MQTT_PORT`
    Mqtt broker port
- `CLIENT_ID`
    Client id

## Mqtt topic

Topic format is `{CLIENT_ID}/toyota/SIGNAL_NAME`

Eg. topic: `student069/toyota/SPEED`  value `34`

## Other 

Thanks for [mitchdetailed](https://github.com/mitchdetailed) for providing tool to convert SocketCAN log with DBC file to csv file. 

[Link to SocketCAN-to-CSV repo](https://github.com/mitchdetailed/SocketCAN-to-CSV)

You can find original log files from [/assets](./assets/) folder in this repo