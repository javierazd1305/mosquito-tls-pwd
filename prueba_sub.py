import paho.mqtt.client as mqtt
import json
from unhash_alg import unhashAlg
# MQTT_HOST = "192.168.0.105"
# localhost
# 8883
# prueba
MQTT_HOST = unhashAlg("(|]+($|_#")
MQTT_PORT = unhashAlg("MMMR")
MQTT_KEEPALIVE_INTERVAL = unhashAlg("P")
MQTT_TOPIC = unhashAlg("/-@}*+")


def on_connect(mosq, obj, rc):
    mqttc.subscribe(MQTT_TOPIC, 0)


def on_subscribe(mosq, obj, mid, granted_on):
    print 'subscribed'


def on_message(mosq, obj, msg):
    print msg.payload


mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.username_pw_set(unhashAlg("+[?%'"), str(unhashAlg("TSRQ")))
# mqttc.tls_insecure_set(True)
# mqttc.tls_set("/usr/local/etc/mosquitto/certs/server.crt")
# mqttc.tls_set("/usr/local/etc/mosquitto/test_certs/certs/server.crt")
mqttc.tls_set(unhashAlg(
    "p@_-p(|]+(p}#]p?|_.@%##|p#}_#s]}-#_p]}-#_p_}-Z}-q]-#"))
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
mqttc.loop_forever()
db.close()
