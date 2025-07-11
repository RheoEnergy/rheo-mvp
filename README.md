# Rheo MVP

## Information
This project simulates power meters communicating with a central node, sending electrical energy data with the central node minting Rheo energy tokens once the accumulated amount of electrical energy exceeds 2 kWh. 

## Installation
Create a new python environment. Use `mkvirtualenv`, `venv`, etc.

### Windows
To install on Windows and run using the provided batch files, use venv instead.
`python -m venv venv`
`venv\Scripts\activate`
`pip install -r requirements.txt`

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

## # Rheo Smart Meter MVP

This repository contains the early-stage MVP of Rheo’s smart meter integration system. It demonstrates how real-time energy data (kWh) collected from smart meters is transmitted via MQTT and tokenized into digital assets — forming the foundation of our energy-backed stablecoin (GET).

---

## 🔗 XRPL Integration (Planned)

This MVP is off-chain, but designed for seamless XRPL integration. We plan to:

- Use **Issued Currencies** to represent GET (Green Energy Token)
- Leverage **XRPL Hooks** (once available) to automate token issuance based on real-time energy thresholds
- Push validated tokenization events to the **XRPL Mainnet** via `xrpl-py`
  
---

## 🔧 Libraries & Frameworks

- **paho-mqtt** – For MQTT communication
- **Python 3.9+** – Language base
- **pytest** – Lightweight test framework (for token logic)
- **(Planned)**: xrpl-py SDK for issuing and tracking GET tokens on XRPL
  
## 📈 System Design Diagram

**Narrative**:  
1. A simulated smart meter pushes verfied energy usage & issuance (kWh) to the MQTT broker.  
2. The MQTT client receives data and logs it.  
3. A converter processes kWh into token units (e.g., 1 kWh = 1 GET).  
4. Tokens are recorded and (in production) will trigger on-chain issuance via XRPL.
          +----------------------+
          |   Energy Producers   |
          |  (Smart Meters, IoT) |
          +----------+-----------+
                     |
          Real-time kWh data via MQTT
                     |
          +----------v-----------+
          |   Rheo Data Engine   |  <-- Data validation, token conversion (kWh → GET)
          +----------+-----------+
                     |
          Token issuance & settlement triggers
                     |
       +-------------v--------------+
       |      XRPL Mainnet          |  <-- Issued Currencies (GET stablecoin), Settlement, Hooks
       +-------------+--------------+
                     |
          +----------v-----------+
          |   XRPL EVM Sidechain |  <-- Smart contracts, staking, governance, liquidity pools
          +----------+-----------+
                     |
          +----------v-----------+
          |    Institutional     |
          |     Investors &      |
          |     Marketplaces     |
          +---------------------+

Optional integrations (dashed lines):
          +-----------------+
          |Other Blockchains| <-- Cross-chain bridges, interoperability (future)
          +-----------------+
          +-----------------+
         |RTGS/OTC/CEX & DeFi| <-- Liquidity, compliance, market access
          +-----------------+

## 🚧 Status & Roadmap

✅ Basic MQTT-to-kWh logic  
✅ Token unit mapping  
🔜 XRPL token issuance via `xrpl-py`  
🔜 Smart contract logic via XRPL Hooks  
🔜 Energy partner pilot integration  

---

## 🧠 About Rheo

Rheo is building the first institutional-grade, blockchain-based investment platform backed by real-world sustainable infrastructure. This MVP is part of our energy tokenisation pipeline, designed for future deployment on the XRPL.

---

## 🚧 Status & Roadmap

✅ Basic MQTT-to-kWh logic  
✅ Token unit mapping  
🔜 XRPL token issuance via `xrpl-py`  
