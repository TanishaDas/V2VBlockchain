import hashlib
import datetime

class Block:
    def __init__(self, index, timestamp, previous_hash, messages):
        self.index = index
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.messages = messages
        self.nonce = ""
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        data_to_hash = str(self.index) + str(self.timestamp) + str(self.previous_hash) + str(self.messages) + self.nonce
        hash_object = hashlib.sha256(data_to_hash.encode())
        return hash_object.hexdigest()

    def mine_block(self, difficulty):
        target = "0" * difficulty

        while not self.hash[:difficulty] == target:
            self.nonce = str(datetime.datetime.now().timestamp())
            self.hash = self.calculate_hash()

        print("Block mined: " + self.hash)

class Blockchain:
    def __init__(self, difficulty):
        self.chain = []
        self.members = []
        self.difficulty = difficulty
        self.chain.append(self.create_genesis_block())

    def create_genesis_block(self):
        messages = ["Genesis block"]
        return Block(0, datetime.datetime.now(), "0", messages)

    def add_member(self, member):
        self.members.append(member)

    def add_block(self, messages):
        latest_block = self.chain[-1]
        new_block = Block(latest_block.index + 1, datetime.datetime.now(), latest_block.hash, messages)
        new_block.mine_block(self.difficulty)
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if not current_block.hash == current_block.calculate_hash():
                return False

            if not current_block.previous_hash == previous_block.hash:
                return False

        return True

class SecureContract:
    def __init__(self, sender, recipient, amount):
        self.sender = sender
        self.recipient = recipient
        self.amount = amount

    def get_sender(self):
        return self.sender

    def get_recipient(self):
        return self.recipient

    def get_amount(self):
        return self.amount

if __name__ == "__main__":
    blockchain = Blockchain(4)

    num_vehicles = int(input("Enter the number of vehicles participating in V2V communication: "))

    for i in range(num_vehicles):
        vehicle = input("Enter the name of vehicle {}: ".format(i + 1))
        blockchain.add_member(vehicle)

    while True:
        print("\nMenu:")
        print("1. Send a message between vehicles")
        print("2. Print the V2V communication blockchain")
        print("3. Exit")
        choice = int(input("Enter your choice: "))

        if choice == 1:
            sender_index = int(input("Enter the index of the sender vehicle (1-{}): ".format(num_vehicles)))
            if sender_index < 1 or sender_index > num_vehicles:
                print("Invalid vehicle index.")
                continue

            recipient_index = int(input("Enter the index of the recipient vehicle (1-{}): ".format(num_vehicles)))
            if recipient_index < 1 or recipient_index > num_vehicles:
                print("Invalid vehicle index.")
                continue

            message = input("Enter the message: ")

            messages = ["From Vehicle {} to Vehicle {}: {}".format(sender_index, recipient_index, message)]
            blockchain.add_block(messages)

        elif choice == 2:
            print("\nV2V Communication Blockchain Status:")
            print("Blockchain is valid:", blockchain.is_chain_valid())

            for block in blockchain.chain:
                print("\nBlock Index:", block.index)
                print("Timestamp:", block.timestamp)
                print("Previous Hash:", block.previous_hash)
                print("Hash:", block.hash)
                print("Messages:")
                for msg in block.messages:
                    print("- " + msg)

        elif choice == 3:
            break

        else:
            print("Invalid choice.")
