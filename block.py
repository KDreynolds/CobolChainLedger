import hashlib
import time

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce=0):
        self.index = index
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.nonce = nonce
        self.hash = self.compute_hash()

    def compute_hash(self):
        """
        A function that return the hash of the block contents.
        """
        block_string = f"{self.index}{self.transactions}{self.timestamp}{self.previous_hash}{self.nonce}".encode()
        return hashlib.sha256(block_string).hexdigest()

    def proof_of_work(self, difficulty):
        """
        Function that tries different values of nonce to get a hash
        that satisfies our difficulty criteria.
        """
        self.nonce = 0
        computed_hash = self.compute_hash()
        while not computed_hash.startswith('0' * difficulty):
            self.nonce += 1
            computed_hash = self.compute_hash()
        self.hash = computed_hash
        return computed_hash

    def __str__(self):
        return f"Block(Index: {self.index}, Transactions: {self.transactions}, Timestamp: {self.timestamp}, Hash: {self.hash}, PrevHash: {self.previous_hash}, Nonce: {self.nonce})"

# Function to create a genesis block
def create_genesis_block():
    return Block(0, [], time.time(), "0")

# Function to generate a new block given the previous block in the chain
def generate_new_block(previous_block, transactions):
    new_block_index = previous_block.index + 1
    new_block_timestamp = time.time()
    new_block_previous_hash = previous_block.hash
    new_block = Block(new_block_index, transactions, new_block_timestamp, new_block_previous_hash)
    new_block.proof_of_work(difficulty=4)  # Assuming a difficulty level of 4 for the proof of work
    return new_block
