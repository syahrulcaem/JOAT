from .block import Block

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "Genesis Block", "0")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        previous_block = self.get_latest_block()
        new_block = Block(index=previous_block.index + 1,
                          data=data,
                          previous_hash=previous_block.hash)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                print(f"❌ Hash tidak valid di blok {i}")
                return False

            if current.previous_hash != previous.hash:
                print(f"❌ Previous hash tidak cocok di blok {i}")
                return False

        print("✅ Blockchain valid.")
        return True
