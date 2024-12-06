# Rheo MVP

## Information
This project simulates power meters communicating with a central node, sending electrical energy data with the central node minting Rheo energy tokens once the accumulated amount of electrical energy exceeds 2 kWh. 

## Installation
Create a new python environment. Use `mkvirtualenv`, `venv`, etc.

Activate the python environment. Install the prerequisite libraries by `pip install -r requirements.txt`

Rename the `environment.env.sample` environment file to `environment.env`. You need the following environment variables:
- RPC URL: The address of the RPC (Remote Procedure Call) web3 server for this application to connect to.
- Private key: The private key, in hex format, of the web3 wallet this application is connected to.
- Contract address: The address of the (mintable) ERC-20 token contract where the energy tokens reside on.
- MQTT server: Address of MQTT server that will relay the energy reading messages.
- MQTT port: Port of the abovementioned MQTT server.
- Topic: The topic where server and clients publish and subscribe to.

## Instructions
Open 2 (or more) terminal windows at the project folder.

In the first window, type in `python run.py server` and press enter. This will be the central node.

In the next window, type in `python run.py meter` and press enter. This will be the power meter.

It is then possible to see the meters sending and the central node collecting energy data, as well as view the minting transactions sent by the node.
To view the tokens, use wallet software like metamask to see the balance of Rheo tokens in the wallet where this project is configured to mint to. 

Alternatively it is also possible to run the application by copying or pulling this project folder onto the user's desktop folder and copying the two `.desktop` files onto the desktop. Double-clicking on these files will launch either the meter or server scripts.

## To do
Simulate burning of tokens by prepaid meters as electricity flows through them.
