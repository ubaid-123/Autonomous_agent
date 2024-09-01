# Autonomous Agent

- Agent 1: Listens for incoming connections, accepts connections, and maintains communication with clients. It generates random messages, sends them to clients, and processes incoming messages.
  
- Agent 2: Connects to the server, communicates by sending and receiving messages, generates random messages, and processes incoming messages.

In essence, both agents are capable of sending and receiving messages, making them act as both client and server depending on the context of the communication. Agent 1 primarily acts as a server that listens for connections, while Agent 2 primarily acts as a client that initiates the connection. Once the connection is established, they can both send and receive messages, making them clients and servers for each other in terms of message exchange.

# How to run this?
python agent1.py
python agent2.py

# Unit test and integration
python -m unittest .\tests\testBaseAgent.py
python -m unittest .\tests\testIntegrationAgents.py
