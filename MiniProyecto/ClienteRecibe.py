import paho.mqtt.client as mqtt
import inspect

host = "127.0.0.1"
nclienteB = "Receptor"
topico = "msj"

def on_message_recibe(client, userdata, message):
    print("message "+str(message.payload.decode("utf-8")))
    if message.payload.decode("utf-8") != " ":
        archivo = open("prueba.txt","a") 
        archivo.write(message.payload.decode("utf-8")+"\n")
        archivo.close()
    else:
        print("hubo un error")

def on_disconnect(client, userdata, rc):
    if rc == 1:
        print("Error en la conexió")
        cliente.loop_stop()

cliente = mqtt.Client(client_id=nclienteB, clean_session=True, userdata=None, protocol=4, transport="tcp")
cliente.on_message = on_message_recibe
cliente.on_disconnect = on_disconnect
cliente.connect(host)
cliente.subscribe(topico,qos=1)

cliente.loop_start()
cliente.loop_stop()
cliente.disconnect()
