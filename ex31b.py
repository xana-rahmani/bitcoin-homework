from utils import *
from config import (my_private_key, my_public_key, my_address, faucet_address, network_type)
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret, P2PKHBitcoinAddress

from ex1 import P2PKH_scriptPubKey
from ex31a import Q31a_txout_scriptPubKey


farazPrivate = CBitcoinSecret('cTGams7K1oxBoDkjRvDJSrmgz3de4KfPjC7e6VWEMEK2jDM9Wj8o')
farazPublic = farazPrivate.pub
faraz_address = P2PKHBitcoinAddress.from_pubkey(farazPublic)

ataPrivate = CBitcoinSecret('cQEiEmMM9T8RyPQCaMxcejNLfuoyeb4ov53s6CztzD72sSrDciLf')
ataPublic = ataPrivate.pub
ata_address = P2PKHBitcoinAddress.from_pubkey(ataPublic)

''' shareholders '''
s1Private = CBitcoinSecret('cPurxNpcyUM6GFpERmpFQKR1QmL11NDfqGqBRZgRZKgvAGUrBJfg')
s1public = s1Private.pub
s1_address = P2PKHBitcoinAddress.from_pubkey(s1public)

s2Private = CBitcoinSecret('cVdmsf92tzUNeXP44Jo1hdR8PNL7Hm45Hve7k7xxZxh2FKjKHjYr')
s2public = s2Private.pub
s2_address = P2PKHBitcoinAddress.from_pubkey(s2public)

s3Private = CBitcoinSecret('cRi1r6WujMseDfxoxK9K5NYKaPkbxvCKW53Lj4Du4qUS6iuW6dXN')
s3public = s3Private.pub
s3_address = P2PKHBitcoinAddress.from_pubkey(s3public)


s4Private = CBitcoinSecret('cVFdd1BxKB7hsD819dtekTKiuVscqtBZWCL88xu1S2j5f9ASveSm')
s4public = s4Private.pub
s4_address = P2PKHBitcoinAddress.from_pubkey(s4public)

s5Private = CBitcoinSecret('cT32H7UbSFtEnAzHMVVVMjNC5RhnH9JuitV5EqkYrEzvQ6od9nkv')
s5public = s5Private.pub
s5_address = P2PKHBitcoinAddress.from_pubkey(s5public)

amount_to_send = 0.00001  # amount of BTC in the output you're splitting minus fee
txid_to_spend = ('a71a78de86f6e347139d488ab6a87267ecf77f9436a255a2783217a477b7f7c8')
utxo_index = 0  # index of the output you are spending, indices start at 0


txin_scriptPubKey = Q31a_txout_scriptPubKey
txin = create_txin(txid_to_spend, utxo_index)
txout_scriptPubKey = P2PKH_scriptPubKey(faucet_address)
txout = create_txout(amount_to_send, txout_scriptPubKey)

faraz_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, farazPrivate)
ata_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, ataPrivate)

s1_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, s1Private)
s2_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, s2Private)
s3_signature = create_OP_CHECKSIG_signature(txin, txout, txin_scriptPubKey, s3Private)


txin_scriptSig = [ata_signature, faraz_signature]

response = send_from_custom_transaction(
    amount_to_send, txid_to_spend, utxo_index,
    txin_scriptPubKey, txin_scriptSig, txout_scriptPubKey, network_type)
print(response.status_code, response.reason)
print(response.text)
