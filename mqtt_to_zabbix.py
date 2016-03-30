#!/usr/bin/env python

import paho.mqtt.client as paho
from pyzabbix import ZabbixMetric, ZabbixSender

# mqtt broker parameters
mqtt_host = "127.0.0.1"
mqtt_topic = "amq.topic"

#zabbix server parameters
# you must create host and item in zabbix (item type - zabbix trapper)
zabbix_host = "127.0.0.1"
zabbix_item_host = "myself"
zabbix_item_name = "Temperature"




def on_message(client, userdata, msg):
    packet = [
      ZabbixMetric(zabbix_item_host, zabbix_item_name, str(msg.payload)),
    ]
    sender = ZabbixSender(zabbix_server=zabbix_host, zabbix_port=10051, use_config=None)
    sender.send(packet)

client = paho.Client()
client.on_message = on_message
client.connect(mqtt_host, 1883)
client.subscribe(mqtt_topic, qos=1)
 
client.loop_forever()
