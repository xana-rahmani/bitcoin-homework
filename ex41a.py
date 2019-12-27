from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret, P2PKHBitcoinAddress
from config import (my_private_key, my_public_key, my_address, faucet_address, network_type)
from ex1 import send_from_P2PKH_transaction

hamedPrivate = CBitcoinSecret('cN2uenBHn5HYKExZHvwj5rj8nNKjrSxM68diEvfrHwkjzKXf4afx')
hamedPublic = hamedPrivate.pub
hamed_address = P2PKHBitcoinAddress.from_pubkey(hamedPublic)


OP_CHECKLOCKTIMEVERIFY = CScriptOp(0xb1)
OP_DROP = CScriptOp(0x75)
OP_DUP = CScriptOp(0x76)
OP_HASH160 = CScriptOp(0xa9)
OP_EQUALVERIFY = CScriptOp(0x88)
OP_CHECKSIG = CScriptOp(0xac)

expiry_time = 1577451600  # (https://www.epochconverter.com/) Friday, December 27, 2019 1:00:00 PM

Q41a_txout_scriptPubKey = [expiry_time, OP_CHECKLOCKTIMEVERIFY, OP_DROP, OP_DUP, OP_HASH160, hamed_address, OP_EQUALVERIFY, OP_CHECKSIG]


if __name__ == '__main__':
    amount_to_send = 0.0003
    txid_to_spend = ('4f524dfdfdf4ff29369dd815066848ebcc4cc62bb12c33765462f6134e924691')
    utxo_index = 1

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q41a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
