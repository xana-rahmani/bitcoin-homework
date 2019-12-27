from bitcoin.core.script import *

######################################################################
# These functions will be used by Alice and Bob to send their respective
# coins to a utxo that is redeemable either of two cases:
# 1) Recipient provides x such that hash(x) = hash of secret
#    and recipient signs the transaction.
# 2) Sender and recipient both sign transaction
#
# TODO: Fill these in to create scripts that are redeemable by both
#       of the above conditions.
# See this page for opcode documentation: https://en.bitcoin.it/wiki/Script


# This is the ScriptPubKey for the swap transaction
def coinExchangeScript(public_key_sender, public_key_recipient, hash_of_secret):
    return [
        CScriptOp(0x76),CScriptOp(0xa9),hash_of_secret,CScriptOp(0x87),CScriptOp(0x63),CScriptOp(0x75),public_key_recipient,CScriptOp(0xac),CScriptOp(0x67),0,2,
        public_key_sender,public_key_recipient,2,CScriptOp(0xae),CScriptOp(0x68)
    ]
# dup hash160 <hash> equal op_if op drop publicbob checksig op_else 0 2 pubalice pubbob 2 checkmultisig end_if
#
# accepted inputs:
# [sigbob,x]
#
# [sigbob,sigalice]
#
# the 2 to 1 multisig is for case 1 input
# This is the ScriptSig that the receiver will use to redeem coins
def coinExchangeScriptSig1(sig_recipient, secret):
    return [
        sig_recipient,secret
    ]

# This is the ScriptSig for sending coins back to the sender if unredeemed
def coinExchangeScriptSig2(sig_sender, sig_recipient):
    return [
        sig_recipient,sig_sender
    ]
######################################################################

######################################################################
#
# Configured for your addresses
#
# TODO: Fill in all of these fields
#

alice_txid_to_spend     = "eeee77101a4fa761a1633e7064c540bd476677b0c6d4225bafba9da65b926c12"
alice_utxo_index        = 1
alice_amount_to_send    = 0.0002

bob_txid_to_spend       = "238b90a111a5e109b736cc778fb8169b3349378c8c25190a279089c18c6bc96b"
bob_utxo_index          = 0
bob_amount_to_send      = 0.05

# Get current block height (for locktime) in 'height' parameter for each blockchain (and put it into swap.py):
#  curl https://api.blockcypher.com/v1/btc/test3
btc_test3_chain_height  = 1635771

#  curl https://api.blockcypher.com/v1/bcy/test
bcy_test_chain_height   = 2676431

# Parameter for how long Alice/Bob should have to wait before they can take back their coins
## alice_locktime MUST be > bob_locktime
alice_locktime = 5
bob_locktime = 3

tx_fee = 0.0001

# While testing your code, you can edit these variables to see if your
# transaction can be broadcasted succesfully.
broadcast_transactions = False
alice_redeems = False

######################################################################
