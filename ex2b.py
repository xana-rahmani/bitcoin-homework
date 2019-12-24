from sys import exit
from bitcoin.core.script import *
from utils import *
from config import (my_private_key, my_public_key, my_address, faucet_address, network_type)
from ex1 import P2PKH_scriptPubKey
from ex2a import Q2a_txout_scriptPubKey


amount_to_send = 0.000007  # amount of BTC in the output you're splitting minus fee
txid_to_spend = ('d53bbdb8a55c66946e85b199c29bcf4100c0e66a0ff3f73fe30ae240460f5a4a')
utxo_index = 0  # index of the output you are spending, indices start at 0


txin_scriptPubKey = Q2a_txout_scriptPubKey
txin_scriptSig = [7547, 1963]
txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)

response = send_from_custom_transaction(
    amount_to_send, txid_to_spend, utxo_index,
    txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey, network_type)
print(response.status_code, response.reason)
print(response.text)
