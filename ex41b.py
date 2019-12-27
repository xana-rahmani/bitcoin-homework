from utils import *
from config import (my_private_key, my_public_key, my_address, faucet_address, network_type)
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret, P2PKHBitcoinAddress

from ex1 import P2PKH_scriptPubKey
from ex41a import Q41a_txout_scriptPubKey


hamedPrivate = CBitcoinSecret('cN2uenBHn5HYKExZHvwj5rj8nNKjrSxM68diEvfrHwkjzKXf4afx')
hamedPublic = hamedPrivate.pub
hamed_address = P2PKHBitcoinAddress.from_pubkey(hamedPublic)

amount_to_send = 0.00009  # amount of BTC in the output you're splitting minus fee
txid_to_spend = ('4a785ca2113824cbc74cc0fa1613cdf66e3954d19f90b84486f1d23e04dfd538')
utxo_index = 0  # index of the output you are spending, indices start at 0

# in 12:17  = {"error": "Error validating transaction: Error running script for input 0 referencing 577c406b37f20c531d6e58e8b20bd78a56f1c82df12b90cfc3df83c4f2de71c5 at 0: Script was NOT verified successfully.."}

txin_scriptPubKey = Q41a_txout_scriptPubKey
txin = create_txin(txid_to_spend, utxo_index)
txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)
txout = create_txout(amount_to_send, txout_scriptPubKey)

hamedPrivate = CBitcoinSecret('cN2uenBHn5HYKExZHvwj5rj8nNKjrSxM68diEvfrHwkjzKXf4afx')
hamedPublic = hamedPrivate.pub

hamed_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, hamedPrivate)

txin_scriptSig = [hamed_signature, hamedPublic]

response = send_from_custom_transaction(
    amount_to_send, txid_to_spend, utxo_index,
    txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey, network_type)
print(response.status_code, response.reason)
print(response.text)
