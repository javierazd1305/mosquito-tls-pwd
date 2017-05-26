import paho.mqtt.client as mqtt
import json
import MySQLdb
import datetime
import smtplib
from unhash_alg import unhashAlg


#<-------CONFIG--------->
MQTT_HOST = unhashAlg("(|]+($|_#")  # "localhost"
MQTT_PORT = 8883
MQTT_KEEPALIVE_INTERVAL = 5
MQTT_TOPIC = unhashAlg("Y%((")  # "will"

MQTT_username = unhashAlg("+[?%'")  # admin
MQTT_pass = str(unhashAlg("TSRQ"))  # 1234
MQTT_tls_path = unhashAlg(
    "p@_-p(|]+(p}#]p?|_.@%##|p#}_#s]}-#_p]}-#_p_}-Z}-q]-#")  # "/usr/local/etc/mosquitto/test_certs/certs/server.crt"

sql_host = unhashAlg("(|]+($|_#")  # localhost
sql_user = unhashAlg("+[?%'")  # admin
sql_pass = str(unhashAlg("TSRQ"))  # 1234
sql_db = unhashAlg("Z}$%](}s]|@'#}-")  # vehicle_counter

email_user = unhashAlg("&+Z%}-+V[TRUPu!?+%(q]|?")  # correo de inicio
email_pass = unhashAlg("?%!@}(USTU")  # contrasena
correo = False
#<-------CONFIG--------->


def on_connect(mosq, obj, rc):
    mqttc.subscribe(MQTT_TOPIC, 0)


def on_subscribe(mosq, obj, mid, granted_on):
    print 'subscribed'


def on_message(mosq, obj, msg):
    print msg.payload
    mensaje = msg.payload
    json_decoded = json.loads(mensaje)
    counter_id = json_decoded['id']
    time = datetime.datetime.now().strftime('%H.%M')

    db = MySQLdb.connect(host=sql_host,
                         user=sql_user,
                         passwd=sql_pass,
                         db=sql_db)

    cursor = db.cursor()
    content = 'el sensor con id ' + \
        str(counter_id) + ' se ha desconectado ' + time
    subject = 'sensor desconectado'
    message = 'Subject: {}\n\n{}'.format(subject, content)

    try:
        cursor.execute(
            """UPDATE sensors SET status = 0, last_offline=now() where id = %d""" % counter_id)
        db.commit()
        print content

    except:
        print 'no hecho'
        db.rollback()
    if correo:
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login(email_user, email_pass)
        mail.sendmail(email_user,
                      email_user, message)
        mail.close()


mqttc = mqtt.Client()
mqttc.on_message = on_message
mqttc.username_pw_set(MQTT_username, MQTT_pass)
# mqttc.tls_set("/usr/local/etc/mosquitto/certs/server.crt")
mqttc.tls_set(MQTT_tls_path)
mqttc.on_connect = on_connect
mqttc.on_subscribe = on_subscribe
mqttc.connect(MQTT_HOST, MQTT_PORT, MQTT_KEEPALIVE_INTERVAL)
mqttc.loop_forever()
db.close()
