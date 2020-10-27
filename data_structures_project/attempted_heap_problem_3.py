import sys
import operator


class Node:
    def __init__(self, value=1):
        self.left = None
        self.right = None
        self.letter = None
        self.value = value
        self.binary = ''

    def set_value(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_left_child(self, node):
        self.left = node

    def set_right_child(self, node):
        self.right = node

    def get_left_child(self):
        return self.left

    def get_right_child(self):
        return self.right

    def has_left_child(self):
        return self.left is not None

    def has_right_child(self):
        return self.right is not None


class Tree:
    def __init__(self, node):
        self.root = node

    def get_root(self):
        return self.root

class Heap:
    def __init__(self, initial_size):
        self.tree = [None for _ in range(initial_size)] # initialize arrays
        self.next_index = 0 # denotes next index where new element should go

    
    def insert(self, data):
        self.tree[self.next_index] = data
        self.up_heapify()
        self.next_index += 1
        if len(self.tree) >= self.next_index:
            arr_copy = self.tree
            self.tree = [None for _ in range(2 * len(self.tree))]
            for idx in range(self.next_index):
                self.tree[idx] = arr_copy[idx]

    
    def up_heapify(self):
        child_index = self.next_index
        while child_index >= 1:
            parent_index = (child_index - 1) // 2
            child_elem = self.tree[child_index]
            parent_elem = self.tree[parent_index]
            
            if child_elem.value < parent_elem.value:
                self.tree[parent_index] = child_elem.value
                self.tree[child_index] = parent_elem.value
                child_index = parent_index
            else:
                break

    def size(self):
        return self.next_index


def find_frequencies(data):
    if data == '':
        return None
    # determine relevant frequencies
    freq_dict = {}
    for char in data:
        if char not in freq_dict:
            freq_dict[char] = 1
        else:
            freq_dict[char] += 1
    return freq_dict


def sort_freq_dict(freq_dict):
    sorted_dict = []
    # build sorted list of tuples from lowest to highest frequencies
    for kv in sorted(freq_dict.items(), key=lambda kv: (kv[1], kv[0])):
        sorted_dict.append((kv))
    # create list of nodes from tuples
    return sorted_dict


def build_huffman_llist(sorted_dict, nodes_list):
    # create ordered list of Nodes for tree
    for item in range(len(sorted_dict)):
        node_data = sorted_dict.pop(0)
        new_node = Node(node_data[1])
        new_node.letter = node_data[0]
        new_node.freq = node_data[1]
        nodes_list.append(new_node)
    return nodes_list


def build_huffman_tree(nodes_list):
    # link nodes to form Huffman tree
    huffman_heap = Heap(len(nodes_list))
    while len(nodes_list) > 1:
        huffman_heap.insert(nodes_list.pop(0))
    huffman_tree = Tree(huffman_heap.tree[0])
    return huffman_tree


def encode_huffman_tree(tree):
    visit_order = []
    root = tree.get_root()
    binary_code = ''

    def add_binary_codes(node, binary_code):
        # attach binary codes to nodes
        if node:
            if node.has_left_child():
                add_binary_codes(node.get_left_child(), binary_code + '0')
            if node.has_right_child():
                add_binary_codes(node.get_right_child(), (binary_code + '1'))
            node.binary = binary_code
            visit_order.append(node.value)
    add_binary_codes(root, binary_code)
    return tree


def trim_tree(tree):
    root = tree.get_root()

    def remove_freqs(node):
        # remove frequency data from nodes
        if node:
            remove_freqs(node.get_left_child())
            remove_freqs(node.get_right_child())
            node.freq = None
    remove_freqs(root)
    return tree


def return_codes_dict(tree):
    if tree is None:
        return None
    codes_dict = {}
    root = tree.get_root()

    def build_codes_dict(node):
        if node:
            build_codes_dict(node.get_left_child())
            build_codes_dict(node.get_right_child())
            if node.letter:
                codes_dict[node.letter] = node.binary
    build_codes_dict(root)
    return codes_dict

def single_char_input(data):
    encoded_string = ''
    for i in data:
        encoded_string += '0'
    node = Node()
    node.letter = data[0]
    node.binary = 0
    node.value = len(data)
    tree = Tree(node)
    return encoded_string, tree



def huffman_encoding(data):
    if data == '':
        return None
    freq_dict = find_frequencies(data)
    sorted_dict = sort_freq_dict(freq_dict)
    if len(sorted_dict) < 2:
        return (single_char_input(data))
    else:
        nodes_list = []
        nodes_llist = build_huffman_llist(sorted_dict, nodes_list)
        huffman_tree = build_huffman_tree(nodes_llist)
        encoded_tree = encode_huffman_tree(huffman_tree)
        trimmed_tree = trim_tree(encoded_tree)
        codes_dict = return_codes_dict(trimmed_tree)
        encoded_string = ''
        for char in data:
            encoded_string += codes_dict[char]
        return encoded_string, trimmed_tree


def huffman_decoding(encoded_data, tree):
    decoded_string = ''
    curr_node = tree.root
    for i in encoded_data:
        # for cases when the input is comprised of only one letter
        if curr_node.left is None and curr_node.right is None:
            decoded_string += curr_node.letter
            continue
        # for all other cases
        if i is "0":
            curr_node = curr_node.left
        else:
            curr_node = curr_node.right
        if curr_node.left is None and curr_node.right is None:  # at a leaf
            decoded_string += curr_node.letter
            curr_node = tree.root
    return decoded_string


# test case 1 - empty string
if __name__ == "__main__":
    codes = {}

    a_great_sentence = ("")

    encoded_data = huffman_encoding(a_great_sentence)
    print("=======TEST CASE 1=======\n")
    if encoded_data is None:
        print("Empty string returns none: Pass!")
        print("Please try again with a more interesting string.\n")


# test case two - shorter string
if __name__ == "__main__":
    codes = {}

    a_great_sentence = ("A short, but great sentence")

    print("=======TEST CASE 2=======\n")

    print("The size of the data is: {}\n".
          format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".
          format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".
          format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".
          format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".
          format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".
          format(decoded_data))


# test case 3 - longer string
if __name__ == "__main__":
    codes = {}

    a_great_sentence = ("I can't believe this complex chunk of code " +
                        "actually does what I intended! Surely there's " +
                        "a shorter and more efficient way, but I shall " +
                        "revel in my success for now and optimize later.")

    print("=======TEST CASE 3=======\n")

    print("The size of the data is: {}\n".
          format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".
          format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".
          format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".
          format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".
          format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".
          format(decoded_data))


# test case 4 - string only contains one unique letter
if __name__ == "__main__":
    codes = {}

    a_great_sentence = ("ffffffffff")

    print("=======TEST CASE 4=======\n")

    print("The size of the data is: {}\n".
          format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".
          format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".
          format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".
          format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".
          format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".
          format(decoded_data))
