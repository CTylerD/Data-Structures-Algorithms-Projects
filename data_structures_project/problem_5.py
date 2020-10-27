import hashlib
from datetime import datetime


class Blockchain:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_block(self, value):
        if self.head is None:
            self.head = Block(value)
            self.tail = self.head
            return
        new_block = Block(value)
        new_block.prev_hash = self.tail.hash
        self.tail.next = new_block
        self.tail = self.tail.next

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size


class Block:
    def __init__(self, value):
        self.timestamp = datetime.now()
        self.value = value
        self.prev_hash = None
        self.hash_string = self.value +\
                           str(self.timestamp) +\
                           str(self.prev_hash)
        self.hash = calc_hash(self.hash_string)
        self.next = None


def calc_hash(data):
    sha = hashlib.sha256()
    hash_str = data.encode('utf-8')
    sha.update(hash_str)
    return sha.hexdigest()


def make_blockchain(list):
    if len(list) == 0:
        return None
    blockchain = Blockchain()
    for string in list:
        blockchain.add_block(string)
    return blockchain


def validate_chain(bchain, list):
    if bchain is None and list == []:  # empty list case
        return True
    curr_node = bchain.head
    for string in list:
        if string != curr_node.value or curr_node is None:
            return False
        else:
            curr_node = curr_node.next
    curr_node = bchain.head
    while curr_node.next is not None:
        if curr_node.hash != curr_node.next.prev_hash:
            return False
        curr_node = curr_node.next
    return True


# test case 1 - empty list
empty_list = []
test_case_1 = make_blockchain(empty_list)
if validate_chain(test_case_1, empty_list):
    print("Test 1: Pass!")
else:
    print("Test 1: FAIL.")


# test case 2 - list with single item
chain_of_one = ['single_string']
test_case_2 = make_blockchain(chain_of_one)

if validate_chain(test_case_2, chain_of_one):
    print("Test 2: Pass!")
else:
    print("Test 2: FAIL.")


# test case 3 - list with multiple items
three_to_blockchain = ['a_string', 'another_string', 'yet_another_string']
test_case_3 = make_blockchain(three_to_blockchain)

if validate_chain(test_case_3, three_to_blockchain):
    print("Test 3: Pass!")
else:
    print("Test 3: FAIL.")
