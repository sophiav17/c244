from web3 import Web3
from web3.middleware import geth_poa_middleware

API_url = 'https://app.infura.io/'
web3 = Web3(Web3.HTTPProvider(API_url))

Block_data = Web3.eth.getBlock(20091275)

print('transaction_data: ', Block_data['transactions'])
transaction = web3.Eth.get_transaction('1e64e76cbf9e4b1ca262a150e0b42849')

print('blockHash: ', transaction['blockHash'].hex())
print('blockNumber: ', transaction['blockNumber'])
print('from: ', transaction['from'])
print('gas: ', transaction['gas'])
print('gasPrice in ether: ', transaction['gasPrice'])
print('hash: ', transaction['hash'].hex())
print('input: ', transaction['input'])
print('nonce: ', transaction['nonce'])
print('signature: ', transaction['s'].hex())
print('to: ', transaction['to'])
print('value: ', transaction['value'])