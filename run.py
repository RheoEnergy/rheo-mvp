import sys
import os
from dotenv import load_dotenv
from web3 import Web3, Account
import mqtt_clients

load_dotenv("environment.env")

MQTT_SERVER = os.getenv("MQTT_SERVER")
MQTT_PORT = int(os.getenv("MQTT_PORT"))
TOPIC = os.getenv("TOPIC")

RPC_URL = os.getenv("RPC_URL")
PRIVATE_KEY = os.getenv("PRIVATE_KEY")
CONTRACT_ADDR=os.getenv("CONTRACT_ADDR")

# TODO: Initialize web3 stuff here


# Run this script with arguments 'meter' or 'server'
if __name__ == "__main__":
    if sys.argv[1] == 'meter':
        mqtt_clients.run_publish(TOPIC, MQTT_SERVER, MQTT_PORT)
    elif sys.argv[1] == 'server':
        mqtt_clients.run_subscribe(TOPIC, MQTT_SERVER, MQTT_PORT, RPC_URL, PRIVATE_KEY, CONTRACT_ADDR)
    else:
        print("Please run this script with the arguments 'meter' or 'server'")

