from utils import *
from config import (faucet_address, network_type)
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from ex1 import P2PKH_scriptPubKey
from ex42a import Q42a_txout_scriptPubKey


hamedPrivate = CBitcoinSecret('cN2uenBHn5HYKExZHvwj5rj8nNKjrSxM68diEvfrHwkjzKXf4afx')
hamedPublic = hamedPrivate.pub
hamed_address = P2PKHBitcoinAddress.from_pubkey(hamedPublic)

amount_to_send = 0.00009  # amount of BTC in the output you're splitting minus fee
txid_to_spend = ('86c015fa1599484a723c8b1d953a32cdfbfe99655264b15dac2990f09c0844ff')
utxo_index = 0  # index of the output you are spending, indices start at 0


txin_scriptPubKey = Q42a_txout_scriptPubKey
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

# The transaction cannot be spent because we used OP_RETURN.
# error: bitcoin.core.scripteval.EvalScriptError: EvalScript: OP_RETURN called
