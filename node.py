from flask import Flask, request, jsonify
from blockchain.chain import Blockchain

app = Flask(__name__)
blockchain = Blockchain()

@app.route('/chain', methods=['GET'])
def get_chain():
    chain_data = []
    for block in blockchain.chain:
        chain_data.append({
            'index': block.index,
            'timestamp': block.timestamp,
            'data': block.data,
            'nonce': block.nonce,
            'previous_hash': block.previous_hash,
            'hash': block.hash
        })
    return jsonify({'length': len(chain_data), 'chain': chain_data})

@app.route('/mine', methods=['POST'])
def mine_block():
    data = request.get_json()
    transactions = data.get("transactions", [])
    blockchain.add_block(transactions)
    return jsonify({"message": "Blok berhasil ditambang!"}), 201

@app.route('/validate', methods=['GET'])
def validate():
    valid = blockchain.is_chain_valid()
    return jsonify({'valid': valid})

if __name__ == '__main__':
    app.run(port=5000)
