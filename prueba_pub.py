import paho.mqtt.client as mqtt
from unhash_alg import unhashAlg
import json

data = {
    'id': 'a',
    'entrada': 'a',
    'salida': 'a',
    'contador': 10
}
data1 = {
    'id': 'a',
    'entrada': 'b',
    'salida': 'b',
    'contador': 12
}
json_data1 = json.dumps(data1)
json_data = json.dumps(data)

msgs = []
msgs.append(json_data1)
msgs.append(json_data)


mqttc = mqtt.Client()
mqttc.username_pw_set("admin", "1234")
# mqttc.tls_insecure_set(True)
# mqttc.tls_set(
#    "/usr/local/etc/mosquitto/certs/server.crt")
mqttc.tls_set("/usr/local/etc/mosquitto/test_certs/certs/server.crt")

mqttc.connect("localhost", 8883, 5)
for i in msgs:
    mqttc.publish(unhashAlg("kifvyz"), i)
mqttc.disconnect()
