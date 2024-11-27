# Rheo MVP

## Information
This project simulates power meters communicating with a central node, sending electrical energy data with the central node minting Rheo energy tokens once the accumulated amount of electrical energy exceeds 2 kWh. 

## Installation

## Instructions
Open 2 (or more) terminal windows at the project folder.

In the first window, type in `python run.py server` and press enter. This will be the central node.

In the next window, type in `python run.py meter` and press enter. This will be the power meter.

It is then possible to see the meters sending and the central node collecting energy data, as well as view the minting transactions sent by the node.
To view the tokens, use wallet software like metamask to see the balance of Rheo tokens in the wallet where this project is configured to mint to. 

## To do
Simulate burning of tokens by prepaid meters as electricity flows through them.
