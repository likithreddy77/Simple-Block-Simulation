import hashlib
import time
# basic block structure
class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data  
        self.previous_hash = previous_hash
        self.nonce = 0  
        self.hash = self.calculate_hash()
    def calculate_hash(self):
        content = str(self.index) + str(self.timestamp) + str(self.data) + str(self.previous_hash) + str(self.nonce)
        return hashlib.sha256(content.encode()).hexdigest()

genesis = Block(0, time.time(), "First block(Genesis Block)", "0")
b1 = Block(1, time.time(), "Some data for block 1", genesis.hash)
b2 = Block(2, time.time(), "Block 2 Data", b1.hash)

chain = [genesis, b1, b2]

print("Original Blockchain:\n")
for blk in chain:
    print(f"Block {blk.index}")
    print(f"Data: {blk.data}")
    print(f"Timestamp: {blk.timestamp}")
    print(f"Nonce: {blk.nonce}")
    print(f"Hash: {blk.hash}")
    print(f"Previous: {blk.previous_hash}\n")

print("\n Tampering Block 1 \n")
b1.data = "Hacked block 1 data!!"
b1.hash = b1.calculate_hash() 

print("Blockchain After Tampering:\n")
for blk in chain:
    print(f"Block {blk.index}")
    print(f"Data: {blk.data}")
    print(f"Timestamp: {blk.timestamp}")
    print(f"Nonce: {blk.nonce}")
    print(f"Hash: {blk.hash}")
    print(f"Previous: {blk.previous_hash}\n")

