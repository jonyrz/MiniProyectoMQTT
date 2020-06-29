import paho.mqtt.client as mqtt
import inspect
import random
import time
import numpy as np
from datetime import datetime

host = "127.0.0.1"
nclienteA = "Emisor"
topico = "msj"
valor = "0"
i=1

def on_message_emisor(client, userdata, message):
    print("Mensaje Enviado " ,str(message.payload.decode("utf-8")))

def on_publish(client, userdata, mid):
    print("Datos de publish")

cliente = mqtt.Client(client_id=nclienteA, clean_session=True, userdata=None, protocol=4, transport="tcp")
cliente.on_message = on_message_emisor
cliente.on_publish = on_publish
cliente.connect(host)
cliente.subscribe(topico,qos=1)

cliente.loop_start()

start_time = datetime.now()
print(start_time)
while i==1:
    valor =random.randrange(10)
    cliente.publish(topic=topico, payload=(valor), qos=1, retain=True, properties=None)
    time.sleep(5)
    time_delta=datetime.now()-start_time
    if time_delta.seconds>=20:
        print(datetime.now())
        break

cliente.loop_stop()
cliente.disconnect()