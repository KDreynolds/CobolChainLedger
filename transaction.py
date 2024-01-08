import time

class Transaction:
    def __init__(self, sender, recipient, amount, timestamp=None):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount
        self.timestamp = timestamp or time.time()

    def to_dict(self):
        """
        Convert the transaction to a dictionary for easier serialization.
        """
        return {
            'sender': self.sender,
            'recipient': self.recipient,
            'amount': self.amount,
            'timestamp': self.timestamp
        }

    def __repr__(self):
        return f"Transaction(Sender: {self.sender}, Recipient: {self.recipient}, Amount: {self.amount}, Timestamp: {self.timestamp})"

# Example usage:
# transaction = Transaction('Alice', 'Bob', 150)
# print(transaction)
# print(transaction.to_dict())
