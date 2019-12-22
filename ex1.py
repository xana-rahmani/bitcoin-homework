from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress

from utils import *
from config import (my_private_key, my_public_key, my_address, faucet_address, network_type)


def P2PKH_scriptPubKey(address):
    OP_DUP = CScriptOp(0x76)
    OP_HASH160 = CScriptOp(0xa9)
    OP_EQUALVERIFY = CScriptOp(0x88)
    OP_CHECKSIG = CScriptOp(0xac)
    return [OP_DUP, OP_HASH160, address, OP_EQUALVERIFY, OP_CHECKSIG]


def P2PKH_scriptSig(txin, txout, txin_scriptPubKey, private_key, public_key):
    signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, private_key)
    return [signature, public_key]


def send_from_P2PKH_transaction(amount_to_send, txid_to_spend, utxo_index, txout_scriptPubKey, sender_private_key, network):

    sender_public_key = sender_private_key.pub
    sender_address = P2PKHBitcoinAddress.from_pubkey(sender_public_key)

    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin_scriptPubKey = P2PKH_scriptPubKey(sender_address)
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = P2PKH_scriptSig(txin, txout, txin_scriptPubKey, sender_private_key, sender_public_key)

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey, txin_scriptSig)

    return broadcast_transaction(new_tx, network)


if __name__ == '__main__':
    amount_to_send = 0.00001  # amount of BTC in the output you're splitting minus fee
    txid_to_spend = ('a1a63ca83a44c193279141e03f1f3d22765ecb4c235d288ba7df8ca05b683e6f')
    utxo_index = 1  # index of the output you are spending, indices start at 0

    txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)
    response = send_from_P2PKH_transaction(
        amount_to_send,
        txid_to_spend,
        utxo_index,
        txout_scriptPubKey,
        my_private_key,
        network_type,
    )
    print(response.status_code, response.reason)
    print(response.text)
