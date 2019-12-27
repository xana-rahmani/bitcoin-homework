from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress
from config import (my_private_key, network_type)
from ex1 import send_from_P2PKH_transaction

hamedPrivate = CBitcoinSecret('cN2uenBHn5HYKExZHvwj5rj8nNKjrSxM68diEvfrHwkjzKXf4afx')
hamedPublic = hamedPrivate.pub
hamed_address = P2PKHBitcoinAddress.from_pubkey(hamedPublic)


OP_DROP = CScriptOp(0x75)
OP_DUP = CScriptOp(0x76)
OP_HASH160 = CScriptOp(0xa9)
OP_EQUALVERIFY = CScriptOp(0x88)
OP_CHECKSIG = CScriptOp(0xac)

message = str('Happy Birthday Hamed').encode()
message = bytes(message)  # b'Happy Birthday Hamed'

Q42a_txout_scriptPubKey = [OP_DUP, OP_HASH160, hamed_address, OP_EQUALVERIFY, OP_CHECKSIG, OP_RETURN, message]

# Hex Ascii Value in blockchain: 48 61 70 70 79 20 42 69 72 74 68 64 61 79 20 48 61 6D 65 64
# Check Ascii from (http://onlinecalculators.brainmeasures.com/Conversions/StringtoAsciiCalculator.aspx)
# learn about Storing data in bitcoin transactions. (https://learnmeabitcoin.com/guide/nulldata)


if __name__ == '__main__':
    amount_to_send = 0.0003
    txid_to_spend = ('919730d4085c0e6fbda6fe305916bab2d7111f0996d89fde291c6c21a1e23827')
    utxo_index = 1

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q42a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
