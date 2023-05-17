import hashlib
import datetime
from project import calculate_hash, create_genesis_block, create_new_block, mine_block

def main():
    test_calculate_hash()
    test_create_genesis_block()
    test_create_new_block()
    test_mine_block()

def test_calculate_hash():
    # Test cases for the calculate_hash function
    assert calculate_hash(0, "0", "2023-01-01", "Genesis Block") == hashlib.sha256("0" + "0" + "2023-01-01" + "Genesis Block").hexdigest()
    assert calculate_hash(1, "previous_hash", "2023-01-02", "Data") == hashlib.sha256("1" + "previous_hash" + "2023-01-02" + "Data").hexdigest()


def test_create_genesis_block():
    # Test case for the create_genesis_block function
    genesis_block = create_genesis_block()
    assert genesis_block.index == 0
    assert genesis_block.previous_hash == "0"
    assert genesis_block.timestamp <= str(datetime.datetime.now())
    assert genesis_block.data == "Genesis Block"
    assert genesis_block.hash == calculate_hash(0, "0",)

def test_create_new_block():
    # Test case for the create_new_block function
    genesis_block = create_genesis_block()
    new_block = create_new_block(genesis_block, "Data")
    assert new_block.index == 1
    assert new_block.previous_hash == genesis_block.hash
    assert new_block.timestamp <= str(datetime.datetime.now())
    assert new_block.data == "Data"
    assert new_block.hash == calculate_hash(1, genesis_block.hash, new_block.timestamp, "Data")


def test_mine_block():
    # Test case for the mine_block function
    genesis_block = create_genesis_block()
    mined_block = mine_block(genesis_block, "Data", 4)
    prefix = "0" * 4
    block_string = str(genesis_block.index + 1) + genesis_block.hash + mined_block.timestamp + "Data" + str(mined_block.nonce)
    hash = hashlib.sha256(block_string.encode()).hexdigest()
    assert hash.startswith(prefix)
    assert mined_block.index == genesis_block.index + 1
    assert mined_block.previous_hash == genesis_block.hash
    assert mined_block.timestamp <= str(datetime.datetime.now())
    assert mined_block.data == "Data"
    assert mined_block.hash == hash

if __name__ == "__main__":
    main()