from bitcoin import SelectParams
from bitcoin.base58 import decode
from bitcoin.core import x
from bitcoin.wallet import CBitcoinAddress, CBitcoinSecret, P2PKHBitcoinAddress


SelectParams('testnet')

faucet_address = CBitcoinAddress('mv4rnyY3Su5gjcDNzbMLKBQkBicCtHUtFB')

# For questions 1-5, we are using 'btc-test3' network. For question 6, you will
# set this to be either 'btc-test3' or 'bcy-test'
network_type = 'bcy-test'


######################################################################
# This section is for Questions 1-5
# TODO: Fill this in with your private key.
#
# Create a private key and address pair in Base58 with keygen.py
# Send coins at https://coinfaucet.eu/en/btc-testnet/

my_private_key = CBitcoinSecret(
    'cUc74jGA9VAPBtSBimEcG4G2y6V4CByNzxF3bzyFrrPvPLXcG7ie')

my_public_key = my_private_key.pub
my_address = P2PKHBitcoinAddress.from_pubkey(my_public_key)

######################################################################


######################################################################
# NOTE: This section is for Question 6
# TODO: Fill this in with address secret key for BTC testnet3
#
# Create address in Base58 with keygen.py
# Send coins at https://coinfaucet.eu/en/btc-testnet/

# Only to be imported by alice.py
# Alice should have coins!!
alice_secret_key_BTC = CBitcoinSecret(
    'cTZkJRn2EEKJv9rCfkpYPv1JoEcE48J5k2E7PfftEueLdLSHL5Rp')

# Only to be imported by bob.py
bob_secret_key_BTC = CBitcoinSecret(
    'cV9Yp34h2Xg8pL9vi7iRjXLbBmB9gaF63Dsmk5Mwrw9oVdwe7w57')

# Can be imported by alice.py or bob.py
alice_public_key_BTC = alice_secret_key_BTC.pub
alice_address_BTC = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BTC)

bob_public_key_BTC = bob_secret_key_BTC.pub
bob_address_BTC = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BTC)
######################################################################


######################################################################
# NOTE: This section is for Question 4
# TODO: Fill this in with address secret key for BCY testnet
#
# Create address in hex with
# curl -X POST https://api.blockcypher.com/v1/bcy/test/addrs?token=$YOURTOKEN
# This request will return a private key, public key and address. Make sure to save these.
#
# Send coins with
# curl -d '{"address": "BCY_ADDRESS", "amount": 1000000}' https://api.blockcypher.com/v1/bcy/test/faucet?token=<YOURTOKEN>
# This request will return a transaction reference. Make sure to save this.

# Only to be imported by alice.py
alice_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('e634a78fa4421cb4df9647c15a7efac7417f4f55d1035a70d731e5414671fbc9'))

# Only to be imported by bob.py
# Bob should have coins!!
bob_secret_key_BCY = CBitcoinSecret.from_secret_bytes(
    x('4c20fe6737be7c3521dcd05fd317283e19a6823957d5b806f96f06611d6b0833'))

# Can be imported by alice.py or bob.py
alice_public_key_BCY = alice_secret_key_BCY.pub
alice_address_BCY = P2PKHBitcoinAddress.from_pubkey(alice_public_key_BCY)

bob_public_key_BCY = bob_secret_key_BCY.pub
bob_address_BCY = P2PKHBitcoinAddress.from_pubkey(bob_public_key_BCY)
######################################################################

# print('my_address: ', my_address)
# print('alice_address_BTC: ', alice_address_BTC)
# print('bob_address_BTC: ', bob_address_BTC)
# print('--------------------------')
# print('bob_address_BCY: ', bob_address_BCY)
# print('alice_address_BCY: ', alice_address_BCY)

# my_address:  n3WtKNZVBpQXgW5xLw9zUcCKGKMotMfH58
# alice_address_BTC:  n3KDxVM3fUhN7rwSzerypyeveNMi8XCrSQ
# bob_address_BTC:  mhcQCHYYBwW6uF5D67EYABF3Z3Xnp4PFqb
# --------------------------
# bob_address_BCY:  msb2WG5XDrw6piXc9V76y1gtFbg2XzmKP8
# alice_address_BCY:  mik9nhJNz4hqcnUrHubQt7S69fMNwb4Anb
