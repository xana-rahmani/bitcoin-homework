from bitcoin.core.script import *


# This is the ScriptPubKey for the swap transaction
def coinExchangeScript(public_key_sender, public_key_recipient, hash_of_secret):
    OP_DUP = CScriptOp(0x76)
    OP_HASH160 = CScriptOp(0xa9)
    OP_EQUAL = CScriptOp(0x87)
    OP_EQUALVERIFY = CScriptOp(0x88)
    OP_CHECKSIG = CScriptOp(0xac)
    OP_CHECKMULTISIG = CScriptOp(0xae)
    OP_IF = CScriptOp(0x63)
    OP_DROP = CScriptOp(0x75)
    OP_ELSE = CScriptOp(0x67)
    OP_ENDIF = CScriptOp(0x68)

    return [
        OP_DUP, OP_HASH160, hash_of_secret, OP_EQUAL,
            OP_IF,
                OP_DROP, public_key_recipient, OP_CHECKSIG,
            OP_ELSE,
                0, 2, public_key_sender, public_key_recipient, 2, OP_CHECKMULTISIG,
            OP_ENDIF
    ]


def coinExchangeScriptSig1(sig_recipient, secret):
    return [sig_recipient, secret]


# This is the ScriptSig for sending coins back to the sender if unredeemed
def coinExchangeScriptSig2(sig_sender, sig_recipient):
    return [sig_recipient, sig_sender]


alice_txid_to_spend = "f09d62591b5504ecd0dcb08aef48251f951204914ae70e5e8b09a037810d5f73"
alice_utxo_index = 0
alice_amount_to_send = 0.0001

bob_txid_to_spend = "9419b26d4b775a82f8f3c03cc60446cbc2956232eb4d73bbbc95f0f7e64a4125"
bob_utxo_index = 0
bob_amount_to_send = 0.001

# Get current block height (for locktime) in 'height' parameter for each blockchain (and put it into swap.py):
# curl https://api.blockcypher.com/v1/btc/test3
btc_test3_chain_height = 1635994

# curl https://api.blockcypher.com/v1/bcy/test
bcy_test_chain_height = 2677863

# Parameter for how long Alice/Bob should have to wait before they can take back their coins
''' alice locktime MUST be > bob locktime '''
alice_locktime = 5
bob_locktime = 3

tx_fee = 0.0001

# While testing your code, you can edit these variables to see if your
# transaction can be broadcasted succesfully.
broadcast_transactions = False
alice_redeems = False

