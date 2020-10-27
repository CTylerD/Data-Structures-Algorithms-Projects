### problem 1 leftover for checking whether or not item is currently in cache:

if key in self.lru_order:
            self.lru_order.remove(key)



### ADD TO PROBLEM THREE TO PRINT OUT THE TREE

"""
class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enq(self, value):
        new_node = LinkedListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.num_elements += 1

    def deq(self):
        if self.is_empty():
            return None
        temp = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def front(self):
        if self.head is None:
            return None
        return self.head.value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0

### print tree function used to visualize tree during development

def print_tree(tree):
    if tree == None:
        return "The tree is empty!"
    level = 0
    q = Queue()
    visit_order = []
    node = tree.get_root()
    q.enq((node, level))
    while q.size() > 0:
        node, level = q.deq()
        if node == None:
            visit_order.append(('<empty>', level))
        else:
            visit_order.append(((node.value, node.letter, node.binary), level))
            if node.has_left_child():
                q.enq((node.get_left_child(), level + 1))
            else:
                q.enq((None, level + 1))
            if node.has_right_child():
                q.enq((node.get_right_child(), level + 1))
            else:
                q.enq((None, level + 1))
    s = "Tree\n"
    previous_level = -1
    for i in range(len(visit_order)):
        node, level = visit_order[i]
        if level == previous_level:
            s += " | " + str(node)
        else:
            s += "\n" + str(node)
            previous_level = level

    return s


# test case 1
tree = huffman_encoding("hi there")
print(print_tree(tree))

# test case 2
tree = huffman_encoding("")
print(print_tree(tree))

# test case 3
tree = huffman_encoding("here's a longer string, what happens here?")
print(print_tree(tree))
"""







def bfs(tree):
    q = Queue()
    visit_order = []
    node = tree.get_root()
    q.enq(node)
    binary_val = node.binary
    while q.size() > 0:
        
        index = 0
        node = q.deq()
        visit_order.append((node.value, node.letter))
        if node.has_left_child():
            binary_val += '0'
            q.enq(node.get_left_child())
        if node.has_right_child():
            binary_val += '1'
            q.enq(node.get_right_child())
        node.binary = binary_val
        print(node.binary)
    return visit_order

        


post_order(tree)

"""
    def traverse(node, binary_counter):
        visit_order = list()
        
        binary_counter_list = []
        if node:
            if node.left.letter != None:
                binary_counter += "0"
                traverse(node.get_left_child(), binary_counter)
            else:
                binary_counter = binary_counter[0:-1]
            if node.right.letter != None:
                binary_counter += "1"
                traverse(node.get_right_child(), binary_counter)
            else:
                binary_counter = binary_counter[0:-1]
            
            visit_order.append(node.get_value)
            binary_counter_list += binary_counter
            print(visit_order)

    traverse(root, binary_counter)
    return visit_order


post_order(tree)
"""


def post_order(tree):
    visit_order = []
    root = tree.get_root()
    

    def traverse(node):
        visit_order = list()
        binary_counter = ''
        if node.left or node.left in visit_order:
            binary_counter += '1'
            print(binary_counter)
        else:
            binary_counter = binary_counter[:-1]
        if node.right:
            binary_counter += '0'
            print(binary_counter)
        else:
            binary_counter = binary_counter[:-1]

        
        
        if node:
            if node.left:
                traverse(node.get_left_child())
            if node.right:
                traverse(node.get_right_child())
            visit_order.append(node)
            print(binary_counter)

    traverse(root)
    return visit_order




class Stack():
    def __init__(self):
        self.list = list()
        
    def push(self,value):
        self.list.append(value)
        
    def pop(self):
        return self.list.pop()
        
    def top(self):
        if len(self.list) > 0:
            return self.list[-1]
        else:
            return None
        
    def is_empty(self):
        return len(self.list) == 0
    
    def __repr__(self):
        if len(self.list) > 0:
            s = "<top of stack>\n_________________\n"
            s += "\n_________________\n".join([str(item) for item in self.list[::-1]])
            s += "\n_________________\n<bottom of stack>"
            return s
        
        else:
            return "<stack is empty>"




### WORKING SOLUTION - CHANGING TO RECURSIVE SOLUTION

import sys, operator

class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class Node:
    def __init__(self, value = 1):
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
        return self.left != None

    def has_right_child(self):
        return self.right != None

class Tree:

    def __init__(self, node):
        self.root = node

    def get_root(self):
        return self.root


class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
        self.num_elements = 0

    def enq(self, value):
        new_node = LinkedListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.num_elements += 1

    def deq(self):
        if self.is_empty():
            return None
        temp = self.head.value
        self.head = self.head.next
        self.num_elements -= 1
        return temp

    def front(self):
        if self.head is None:
            return None
        return self.head.value

    def size(self):
        return self.num_elements

    def is_empty(self):
        return self.num_elements == 0


def huffman_encoding(data):
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
    # build list of tuples from lowest to highest frequencies
    for kv in sorted(freq_dict.items(), key = lambda kv:(kv[1], kv[0])):
        sorted_dict.append((kv))
    # create list of nodes from tuples
    nodes_list = []
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
        nodes_list = sorted(nodes_list, key = operator.attrgetter('value'))
        #build_huffman_tree(nodes_list)
    huffman_tree = Tree(nodes_list[0])
    return huffman_tree

tree = huffman_encoding("hi there")

def huffman_decoding(data,tree):
    pass


# provided by Udacity for testing 
"""
if __name__ == "__main__":
    codes = {}

    a_great_sentence = "The bird is the word"

    print ("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print ("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print ("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print ("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print ("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print ("The content of the encoded data is: {}\n".format(decoded_data))
    """

def print_tree(tree):
    if tree == None:
        return "The tree is empty!"
    level = 0
    q = Queue()
    visit_order = []
    node = tree.get_root()
    q.enq((node, level))
    while q.size() > 0:
        node, level = q.deq()
        if node == None:
            visit_order.append(('<empty>', level))
        else:
            visit_order.append((node.value, level))
            if node.has_left_child():
                q.enq((node.get_left_child(), level + 1))
            else:
                q.enq((None, level + 1))
            if node.has_right_child():
                q.enq((node.get_right_child(), level + 1))
            else:
                q.enq((None, level + 1))
    s = "Tree\n"
    previous_level = -1
    for i in range(len(visit_order)):
        node, level = visit_order[i]
        if level == previous_level:
            s += " | " + str(node)
        else:
            s += "\n" + str(node)
            previous_level = level

    return s


# test case 1
tree = huffman_encoding("hi there")
print(print_tree(tree))

# test case 2
tree = huffman_encoding("")
print(print_tree(tree))

# test case 3
tree = huffman_encoding("my what a rather long string this wound up being, I wonder how large the tree will be")
print(print_tree(tree))
