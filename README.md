# COBOL-Python Blockchain Ledger

This project integrates a COBOL-based financial transaction ledger with a Python-implemented blockchain to provide an immutable record of financial transactions. This ensures that all entries in the ledger can be audited with confidence, as each transaction is recorded in a block within the blockchain, which is then linked to previous transactions, creating a secure chain of records.

## Project Structure

- `block.py`: Defines the `Block` class and includes methods for computing the hash and implementing proof of work.
- `transaction.py`: Defines the `Transaction` class and methods for representing a transaction in a dictionary format.
- `blockchain.py`: Contains the `Blockchain` class that manages the chain of blocks and unconfirmed transactions.
- `ledger.cbl`: The COBOL program that handles the file operations for the financial transactions ledger.
- `ledger_interface.cbl`: The COBOL interface for interacting with the ledger, allowing users to add and read transactions.
- `setup.py`: The setup script for installing the project and its dependencies.
- `utils.py`: Utility functions that support the blockchain functionality (not detailed in the snippets provided).
- `requirements.txt`: A list of Python dependencies required for the blockchain part of the project.
- `README.md`: This file, which provides an overview and instructions for the project.

## Installation

Before running the project, ensure you have COBOL and Python installed on your system. Then, follow these steps:

1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the Python dependencies by running:

```bash
pip install -r requirements.txt
```

4. Compile the COBOL programs (`ledger.cbl` and `ledger_interface.cbl`) using your COBOL compiler.

## Usage

To use the ledger interface:

1. Run the compiled COBOL ledger interface program.
2. Follow the on-screen prompts to add or read transactions.

For the blockchain functionality:

1. The Python scripts can be run individually to test the blockchain functionality.
2. The blockchain is integrated with the COBOL ledger through the Python scripts, which handle the creation of blocks and the addition of transactions to the blockchain.

## Contributing

Contributions to this project are welcome. Please ensure that you follow the existing code structure and maintain the integration between the COBOL ledger and the Python blockchain.

## License

This project is open-source and available under the [MIT License](LICENSE).

## Contact

For any queries or contributions, please contact the project maintainer at your.email@example.com.

## Acknowledgments

This project was created to demonstrate the integration of a traditional COBOL system with modern blockchain technology for secure and auditable financial transactions.
