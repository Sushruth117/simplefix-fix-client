# SimpleFIX FIX Client

This repository contains a Python FIX client using the `simplefix` library for creating and parsing FIX messages.

## Features

- **Send and receive FIX messages**: Basic functionality to send `NewOrderSingle` messages and handle `ExecutionReport` responses.
- **Unit Tests**: Example unit tests for FIX message transactions.

## Installation

To get started, clone the repository and install the dependencies:

```bash
git clone https://github.com/YOUR_GITHUB_USERNAME/simplefix-fix-client.git
cd simplefix-fix-client
pip install -r requirements.txt

## **Overview**
The Financial Information eXchange (FIX) Protocol is a standard way of communicating trade information electronically. It is widely used in the trading industry due to its comprehensive structure, which includes encoding messages, session layer messaging, application layer messaging, and a data dictionary for various trading-related information.

FIX Message Structure
Encoding: ASCII-encoded key-value pairs where keys are integers (tag numbers).
Standard Header and Trailer: Every message starts with tags 8 (BeginString), 9 (BodyLength), and 35 (MsgType) and ends with tag 10 (CheckSum).
Example Message:
css
Copy code
8=FIX.4.2 9=65 35=A 34=1 49=PROOF 52=20210907-12:00:56.460 56=TEST 98=0 108=30 10=009
FIX Session Layer
Session Establishment: Requires a Logon message (35=A) and ends with a Logout message (35=5).
Sequence Numbers: Used for message recovery and maintaining the order of messages.
Heartbeat Messages: Sent periodically to ensure the connection is active.
FIX Application Layer
Order Lifecycle: Involves messages like New Order Single (35=D), ExecutionReport (35=8), Order Cancel/Replace Request (35=G), and Order Cancel Request (35=F).
Domain Model: Defines the structure and content of messages, including various tags and their acceptable values.
FIX Gateways
Functions:

Translation: Converting FIX messages to internal protocols.
Normalization: Handling different FIX dialects.
Validation: Ensuring correct values and formats.
Transformation: Managing parameter conversions for different versions.
