from sys import exit
from bitcoin.core.script import *

from utils import *
from config import (my_private_key, my_public_key, my_address, faucet_address, network_type)
from ex1 import send_from_P2PKH_transaction


# Student_ID = 95105584
OP_2DUP = CScriptOp(0x6e)
OP_ADD = CScriptOp(0x93)
OP_SUB = CScriptOp(0x94)
OP_EQUAL = CScriptOp(0x87)
OP_EQUALVERIFY = CScriptOp(0x88)
Q2a_txout_scriptPubKey = [OP_2DUP, OP_ADD, 9510, OP_EQUALVERIFY, OP_SUB, 5584, OP_EQUAL]

if __name__ == '__main__':
    amount_to_send = 0.00001  # amount of BTC in the output you're splitting minus fee
    txid_to_spend = ('94a6fa3af2b5da3f4e71966add5e3b56616b5cccda24aa2eff2da7dc28e7edc2')
    utxo_index = 0  # index of the output you are spending, indices start at 0

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q2a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
