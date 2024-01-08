import json
import requests

def hash_string_256(string):
    """
    Create a SHA-256 hash of a given string.

    :param string: The string to hash.
    :return: A SHA-256 hash of the string.
    """
    return hashlib.sha256(string.encode()).hexdigest()

def valid_proof(transactions, last_hash, nonce, difficulty):
    """
    Validate the proof by ensuring that it satisfies the difficulty criteria.

    :param transactions: The list of transactions to include in the block.
    :param last_hash: The hash of the previous block in the chain.
    :param nonce: The nonce value that we are testing.
    :param difficulty: The difficulty level of the proof of work.
    :return: True if the proof is valid, False otherwise.
    """
    guess = (str([tx.to_dict() for tx in transactions]) + str(last_hash) + str(nonce)).encode()
    guess_hash = hashlib.sha256(guess).hexdigest()
    return guess_hash[:difficulty] == '0' * difficulty

def broadcast_transaction(transaction, node_list):
    """
    Broadcast a transaction to all nodes in the network.

    :param transaction: The transaction to broadcast.
    :param node_list: The list of nodes to broadcast to.
    """
    for node in node_list:
        try:
            response = requests.post(f'http://{node}/transaction/broadcast', json=transaction.to_dict())
            if response.status_code != 200:
                print(f"Transaction broadcast to {node} failed.")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while broadcasting to {node}: {e}")

def broadcast_block(block, node_list):
    """
    Broadcast a newly mined block to all nodes in the network.

    :param block: The block to broadcast.
    :param node_list: The list of nodes to broadcast to.
    """
    block_data = json.dumps(block.__dict__, sort_keys=True)
    for node in node_list:
        try:
            response = requests.post(f'http://{node}/block/broadcast', json={'block': block_data})
            if response.status_code != 200:
                print(f"Block broadcast to {node} failed.")
        except requests.exceptions.RequestException as e:
            print(f"An error occurred while broadcasting to {node}: {e}")

def verify_transaction_signature(sender_public_key, signature, transaction):
    """
    Check that the provided signature corresponds to transaction
    signed by the public key.

    :param sender_public_key: The public key of the sender.
    :param signature: The signature to verify.
    :param transaction: The transaction that was signed.
    :return: True if the signature is valid, False otherwise.
    """
    # This is a placeholder for signature verification logic.
    # In a real blockchain, you would use the sender's public key and the signature
    # to verify that the transaction has not been tampered with.
    return True
