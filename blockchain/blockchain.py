import time
import hashlib
from .models import PatientData


class Block:
    def __init__(self, index, data, previous_hash):
        self.index = index
        self.timestamp = time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()


    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:
    def __init__(self):
        self.chain = []
        self.create_genesis_block()

    def create_genesis_block(self):
        genesis_block = Block(0, "Genesis Block", "0")
        self.chain.append(genesis_block)

    def get_last_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_hash = self.chain[-1].hash if self.chain else '0'
        block = Block(index=len(self.chain), data=data, previous_hash=previous_hash)
        self.chain.append(block)

    def hash_block(self, index, previous_hash, timestamp, data):
        value = str(index) + str(previous_hash) + str(timestamp) + str(data)
        return hashlib.sha256(value.encode('utf-8')).hexdigest()

    def mark_block_as_deleted(self, index):
        if 0 <= index < len(self.chain):
            self.chain[index].data['deleted'] = True

    def get_active_chain(self):
        return [block for block in self.chain if isinstance(block.data, dict) and not block.data.get('deleted', False)]
