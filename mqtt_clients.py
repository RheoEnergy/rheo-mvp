import uuid
import time
import random
from paho.mqtt import client as mqtt_client
from web3_utils import W3Class

register = 0
sleep_time = 3 #seconds

def connect_mqtt(client_id, broker, port):
    def on_connect(client, userdata, flags, rc, properties):
        if rc == 0:
            print("Connected to MQTT Broker!")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id=client_id, callback_api_version=mqtt_client.CallbackAPIVersion.VERSION2)
    # client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def publish(client, topic):
    while True:
        time.sleep(sleep_time)
        msg = f"{random.random()} kWh"
        result = client.publish(topic, msg)
        # result: [0, 1]
        status = result[0]
        if status == 0:
            print(f"Sent {msg} to {topic}")
        else:
            print(f"Failed to send message to {topic}")

def subscribe(client, topic, w3):
    def on_message(client, userdata, msg):
        print(f"Received {msg.payload.decode()} from {msg.topic}")
        global register
        register += float(msg.payload.decode()[:-4])
        
        if register > 2:
            print(f"Minting {register} kWh of RHEO")
            mint_amount = register
            register = 0
            # TODO: Call mint function here
            w3.mint_token(mint_amount)

    client.subscribe(topic)
    client.on_message = on_message

def run_publish(topic, mqtt_server, mqtt_port):
    client_id = f'publish-{uuid.uuid4()}'
    client = connect_mqtt(client_id, mqtt_server, mqtt_port)
    client.loop_start()
    publish(client, topic)
    client.loop_stop()

def run_subscribe(topic, mqtt_server, mqtt_port, rpc_url, private_key, contract_addr):
    client_id = f'subscribe-{uuid.uuid4()}'
    w3 = W3Class(rpc_url, private_key, contract_addr)
    client = connect_mqtt(client_id, mqtt_server, mqtt_port)
    subscribe(client, topic, w3)
    client.loop_forever()

