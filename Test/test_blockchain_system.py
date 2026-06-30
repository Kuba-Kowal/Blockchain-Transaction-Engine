from dataclasses import dataclass
from datetime import datetime
from hashlib import sha256

@dataclass(frozen=True, slots=True)
class Block:
    id: int
    data: Transaction

@dataclass(slots=True, frozen=True)
class Transaction:
    sender: str
    recipient: str
    amount: int
    priv_sig: str

@dataclass(slots=True, frozen=True)
class MinedBlocks:
    pass

@dataclass(slots=True)
class Account:
    username: str
    balance: int
    transactions: dict

    def check_balance(self):
        return self.balance

    def subtract_balance(self, amount):
        self.balance -= amount

    def add_to_balance(self, amount):
        self.balance += amount

@dataclass
class Blockchain:
    transactions: list[Transaction]
    transaction_id: int

    def process_transaction(self, sender, recipient, amount, validation_key) -> True | False:
        validation_keys = [1212, 5678, 9876]

        if validation_key in validation_keys:
            if sender.balance >= amount:
                self.create_transaction_log(Transaction(self.get_transaction_id(), sender.username, recipient.username, amount, datetime.now()))
                sender.subtract_balance(amount)
                recipient.add_to_balance(amount)

                return True
            
        return False

    def get_transaction_id(self):
        self.transaction_id += 1
        return self.transaction_id

    def view_transaction_log(self):
        print(self.transactions)

    def create_transaction_log(self, transaction):
        self.transactions.append(transaction)

def create_transaction(sender_object, recipient_object, amount, priv_sig, blockchain):
    pass # for now

def create_block(transaction_object, blockchain):
    return Block(blockchain.get_transaction_id(), transaction_object)

def mine_block(block):
    nonce = 0
    hash = ""

    while hash[:4] != "0000" and nonce < 10000000: # 10 million
        hash = generate_hash(block, nonce)
        nonce += 1

    if nonce > 10000000:
        return False

    return f"Hash: {hash}, Nonce: {nonce}, Block: {block}"

def generate_hash(block, nonce):
    payload = f"{block.id}{nonce}{block.data}".encode("utf-8")
    return sha256(payload).hexdigest()

blockchain = Blockchain([], 0)

alice = Account("Alice", 100, {})
bob = Account("Bob", 50, {})

block = create_block(Transaction(alice, bob, 50, 123), blockchain)

mined_block = mine_block(block)

if mined_block != False:
    create_transaction()
