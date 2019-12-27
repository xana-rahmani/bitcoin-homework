import codecs
import hashlib
import base58
from ex1 import *
from config import (my_private_key, my_public_key, my_address, faucet_address, network_type)
from bitcoin.wallet import CBitcoinSecret, P2PKHBitcoinAddress

import hashlib


class MerkleTreeCalculator:
    def calculate_merkle_root(self):
        arrHash = [[]]
        for i in range(2):
            f = open('./data'+str(i+1)+'.hex', "r")
            temp = f.read()
            unencoded_string = bytes.fromhex(temp)
            sha256 = hashlib.sha256(unencoded_string)
            hash_256 = sha256.hexdigest()
            arrHash[0].append(hash_256)
        root, n = 0, 0
        while True:
            l = len(arrHash[n])
            if l == 1:
                return arrHash[n]
            if l % 2 == 0:
                arrHash.append([])
                n += 1
                for j in range(0, l, 2):
                    h = hashlib.sha256()
                    temp = arrHash[n-1][j] + arrHash[n-1][j+1]
                    h.update(temp.encode())
                    arrHash[n].append(h.hexdigest())
            if l % 2 != 0:
                arrHash[n].append(arrHash[n][-1])


''' Perform SHA-256 hashing on the data  '''
m = MerkleTreeCalculator()
root = m.calculate_merkle_root()
hash_256 = root[0]

''' Perform RIPEMD-160 hashing on the result of SHA-256  '''
unencoded_string = bytes.fromhex(hash_256)
RIPEMD160 = hashlib.new('ripemd160', unencoded_string)
hash_RIPEMD160 = RIPEMD160.digest()

''' add version '''
# for main 00
address_temp = '6F' + RIPEMD160.hexdigest()

''' add Checksum'''
unencoded_string = bytes.fromhex(address_temp)
sha256 = hashlib.sha256(unencoded_string)
hash_address_temp = sha256.hexdigest()

unencoded_string = bytes.fromhex(hash_address_temp)
sha256 = hashlib.sha256(unencoded_string)
hash_2_address_temp = sha256.hexdigest()

checksum = hash_2_address_temp[:8]
address_temp = address_temp + checksum

''' base 58 '''
unencoded_string = bytes.fromhex(address_temp)
encoded_string = base58.b58encode(unencoded_string)
address = encoded_string.decode("utf-8")
# address = n2TJ2tG7Tz9M8BMvmqMaujmq4QcH2zn2xK

''' send 1 satoshi '''
if __name__ == '__main__':
    amount_to_send = 0.00000001  # amount of BTC in the output you're splitting minus fee
    txid_to_spend = ('925c9fc1ccb14a82f5669610f22fbe9bcb8a1de396fd94eb74a652ec5a1f1ded')
    utxo_index = 7  # index of the output you are spending, indices start at 0

    txout_scriptPubKey = P2PKH_scriptPubKey(P2PKHBitcoinAddress(address))
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
