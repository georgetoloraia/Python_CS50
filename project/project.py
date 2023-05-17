import hashlib
import datetime


class Block:
    def __init__(self, index, previous_hash, timestamp, data, hash):
        self.index = index
        self.previous_hash = previous_hash
        self.timestamp = timestamp
        self.data = data
        self.hash = hash


def calculate_hash(index, previous_hash, timestamp, data):
    # Implementation of hash calculation algorithm
    block_string = str(index) + previous_hash + timestamp + data
    return hashlib.sha256(block_string.encode()).hexdigest()


def create_genesis_block():
    # Create the first block in the blockchain
    return Block(0, "0", str(datetime.datetime.now()), "Genesis Block", calculate_hash(0, "0", str(datetime.datetime.now()), "Genesis Block"))


def create_new_block(previous_block, data):
    # Create a new block in the blockchain
    index = previous_block.index + 1
    timestamp = str(datetime.datetime.now())
    hash = calculate_hash(index, previous_block.hash, timestamp, data)
    return Block(index, previous_block.hash, timestamp, data, hash)


def mine_block(previous_block, data, difficulty):
    # Mine a new block in the blockchain
    prefix = "0" * difficulty
    nonce = 0
    while True:
        timestamp = str(datetime.datetime.now())
        block_string = str(previous_block.index + 1) + previous_block.hash + timestamp + data + str(nonce)
        hash = hashlib.sha256(block_string.encode()).hexdigest()
        if hash.startswith(prefix):
            return Block(previous_block.index + 1, previous_block.hash, timestamp, data, hash)
        nonce += 1


def main():
    # Initialize the blockchain with the genesis block
    blockchain = [create_genesis_block()]

    # Add more blocks to the blockchain
    block = mine_block(blockchain[-1], "Data 1", 4)
    blockchain.append(block)

            # block2 = mine_block(blockchain[-1], "Data 2", 4)
            # blockchain.append(block2)

    # Print the blockchain
    for block in blockchain:
        print(f"Index: {block.index}")
        print(f"Previous Hash: {block.previous_hash}")
        print(f"Timestamp: {block.timestamp}")
        print(f"Data: {block.data}")
        print(f"Hash: {block.hash}")
        print("---------------------")


if __name__ == "__main__":
    main()
