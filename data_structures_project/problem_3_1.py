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
    sorted_dict = []
    # build sorted list of tuples from lowest to highest frequencies
    for kv in sorted(freq_dict.items(), key=lambda kv: (kv[1], kv[0])):
        sorted_dict.append((kv))
    # create list of nodes from tuples
    nodes_list = []
    return build_huffman_llist(sorted_dict, nodes_list)


def build_huffman_llist(sorted_dict, nodes_list):
    # create ordered list of Nodes for tree
    for item in range(len(sorted_dict)):
        node_data = sorted_dict.pop(0)
        new_node = Node(node_data[1])
        new_node.letter = node_data[0]
        new_node.freq = node_data[1]
        nodes_list.append(new_node)
    return build_huffman_tree(nodes_list)


def build_huffman_tree(nodes_list):
    # link nodes to form Huffman tree
    while len(nodes_list) > 1:
        first_item = nodes_list.pop(0)
        second_item = nodes_list.pop(0)
        parent_node = Node(first_item.value + second_item.value)
        parent_node.left = first_item
        parent_node.right = second_item
        nodes_list.append(parent_node)
        nodes_list = sorted(nodes_list, key=operator.attrgetter('value'))
    huffman_tree = Tree(nodes_list[0])
    return encode_huffman_tree(huffman_tree)


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
    return trim_tree(tree)


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


def huffman_encoding(data):
    if data == '':
        return None
    tree = find_frequencies(data)
    codes_dict = return_codes_dict(tree)
    encoded_string = ''
    for char in data:
        encoded_string += codes_dict[char]
    return encoded_string, tree


def huffman_decoding(encoded_data, tree):
    codes_dict = return_codes_dict(tree)
    rebuilt_string = ''
    temp_char = ''
    for digit in encoded_data:
        temp_char += digit
        for key in codes_dict:
            if temp_char == codes_dict[key]:
                rebuilt_string += key
                temp_char = ''
    return rebuilt_string


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
