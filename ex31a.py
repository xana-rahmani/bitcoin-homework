from bitcoin.core.script import *
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret, P2PKHBitcoinAddress
from config import (my_private_key, my_public_key, my_address, faucet_address, network_type)
from ex1 import send_from_P2PKH_transaction

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

OP_2DUP = CScriptOp(0x6e)
OP_CHECKMULTISIG = CScriptOp(0xae)
OP_CHECKMULTISIGVERIFY = CScriptOp(0xaf)
OP_IF = CScriptOp(0x63)
OP_ELSE = CScriptOp(0x67)
OP_EQUAL = CScriptOp(0x87)
OP_ENDIF = CScriptOp(0x68)
Q31a_txout_scriptPubKey = [OP_2DUP, 0, 2, farazPublic, ataPublic, 2, OP_CHECKMULTISIG, OP_IF, 0, 0, OP_EQUAL, OP_ELSE,
                          0, 1, farazPublic, ataPublic, 2, OP_CHECKMULTISIG, OP_IF, 0, 3, s1public, s2public, s3public,
                          s4public, s5public, 5, OP_CHECKMULTISIGVERIFY, OP_ENDIF, OP_ENDIF]

# the signatures of faraz and ata are  on top of the stack
# [sig-faraz, sig-ata]
# >> op2dup 0 2
# [sig-faraz, sig-ata, sig-faraz, sig-ata]
# pubfaraz pubata 2 OP_CHECKMULTISIG
# """ yes ""
# op_IF
#    0 0 op_equal
# ''' return TRUE '''
#
# [sig-faraz, sig-s1, sig-s2, sig-s3]
#     op_else
#       op 2dup 0 1 pubfaraz pubata 2 checkmultisig
#        op_if
#             0 3 pub1 pub2 pub3 pub4 pub5 5 CHECKMULTISIGverify
#             ''' return TRUE '''
#         op_endif
#     op_endif


if __name__ == '__main__':
    amount_to_send = 0.0004
    txid_to_spend = ('13e0f72b0982c03f35d760b368adf78f04e901f948ff98d4913c786767fadaa3')
    utxo_index = 1

    response = send_from_P2PKH_transaction(
        amount_to_send, txid_to_spend, utxo_index,
        Q31a_txout_scriptPubKey, my_private_key, network_type)
    print(response.status_code, response.reason)
    print(response.text)
