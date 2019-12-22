from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress

from utils import *
from config import (my_private_key, my_public_key, my_address, faucet_address, network_type)


def P2PKH_scriptPubKey(address):
    ######################################################################
    # TODO: Complete the standard scriptPubKey implementation for a
    # PayToPublicKeyHash transaction
    #import hashlib
    import base58

    # print('hash256 str: ', hashlib.sha256(address.encode('utf-8')).hexdigest())
    # res = bin(int(address, 16)).zfill(8)
    # h = hex(int(address, 16))
    # hash_hex = hashlib.new('sha256', h.encode('utf-8')).hexdigest()
    # print('hash256 hex: ', hash_hex)
    # pubKeyHash = hashlib.new('ripemd160', hash_hex.encode('utf-8')).hexdigest()
    # binary = bin(int(address, 16))
    # hash_bin = hashlib.new('sha256', binary.encode('utf-8')).hexdigest()
    # print('hash256 bin: ', hash_bin)
    # pubKeyHash = hashlib.new('ripemd160', hash_bin.encode('utf-8')).hexdigest()

    OP_DUP = '76'
    OP_HASH160 = 'a9'
    bytes_to_push = '14'
    pubKeyHash = base58.b58decode_check(address).hex()[2:]
    OP_EQUALVERIFY = '88'
    OP_CHECKSIG = 'ac'
    # ressult = OP_DUP + OP_HASH160 + bytes_to_push + pubKeyHash + OP_EQUALVERIFY + OP_CHECKSIG
    # print('pubKeyHash:', pubKeyHash)
    # print('ressult: ', ressult)
    return [OP_DUP, OP_HASH160, address, OP_EQUALVERIFY, OP_CHECKSIG]
    ######################################################################


def P2PKH_scriptSig(txin, txout, txin_scriptPubKey, private_key, public_key):
    signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey,
                                             private_key)
    ######################################################################
    # TODO: Complete this script to unlock the BTC that was sent to you
    # in the PayToPublicKeyHash transaction.
    return [
        # fill this in!
    ]
    ######################################################################


def send_from_P2PKH_transaction(amount_to_send,
                                txid_to_spend,
                                utxo_index,
                                txout_scriptPubKey,
                                sender_private_key,
                                network):

    sender_public_key = sender_private_key.pub
    sender_address = P2PKHBitcoinAddress.from_pubkey(sender_public_key)

    txout = create_txout(amount_to_send, txout_scriptPubKey)

    txin_scriptPubKey = P2PKH_scriptPubKey(sender_address)
    txin = create_txin(txid_to_spend, utxo_index)
    txin_scriptSig = P2PKH_scriptSig(txin, txout, txin_scriptPubKey,
        sender_private_key, sender_public_key)

    new_tx = create_signed_transaction(txin, txout, txin_scriptPubKey,
                                       txin_scriptSig)

    return broadcast_transaction(new_tx, network)


# if __name__ == '__main__':
#     ######################################################################
#     # TODO: set these parameters correctly
#     amount_to_send = None  # amount of BTC in the output you're splitting minus fee
#     txid_to_spend = (
#         'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
#     utxo_index = None  # index of the output you are spending, indices start at 0
#     ######################################################################
#
#     txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)
#     response = send_from_P2PKH_transaction(
#         amount_to_send,
#         txid_to_spend,
#         utxo_index,
#         txout_scriptPubKey,
#         my_private_key,
#         network_type,
#     )
#     print(response.status_code, response.reason)
#     print(response.text)


P2PKH_scriptPubKey('n3WtKNZVBpQXgW5xLw9zUcCKGKMotMfH58')

