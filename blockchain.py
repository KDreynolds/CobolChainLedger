import hashlib
from block import Block, create_genesis_block, generate_new_block
from transaction import Transaction

class Blockchain:
    def __init__(self):
        self.unconfirmed_transactions = []
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        """
        A function to generate genesis block and append it to
        the chain. The block has index 0, previous_hash as 0, and
        a valid hash.
        """
        genesis_block = create_genesis_block()
        genesis_block.proof_of_work(difficulty=4)
        self.chain.append(genesis_block)

    @property
    def last_block(self):
        return self.chain[-1]

    def add_new_transaction(self, transaction):
        self.unconfirmed_transactions.append(transaction)

    def mine(self):
        """
        This function serves as an interface to add the pending
        transactions to the blockchain by adding them to the block
        and figuring out Proof of Work.
        """
        if not self.unconfirmed_transactions:
            return False

        last_block = self.last_block

        new_block = generate_new_block(last_block, self.unconfirmed_transactions)

        if new_block is not None:
            self.chain.append(new_block)
            self.unconfirmed_transactions = []
            return new_block
        return None

    def is_chain_valid(self):
        """
        A function that checks if the blockchain is valid.
        """
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.compute_hash():
                return False

            if current.previous_hash != previous.hash:
                return False

        return True

    def print_chain(self):
        """
        A helper method to display the blockchain.
        """
        for block in self.chain:
            print(block)

# Example usage:
# blockchain = Blockchain()
# transaction1 = Transaction('Alice', 'Bob', 100)
# blockchain.add_new_transaction(transaction1.to_dict())
# blockchain.mine()
# transaction2 = Transaction('Bob', 'Alice', 50)
# blockchain.add_new_transaction(transaction2.to_dict())
# blockchain.mine()
# blockchain.print_chain()
# print("Blockchain validity:", blockchain.is_chain_valid())

