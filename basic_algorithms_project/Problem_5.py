from ipywidgets import widgets
from IPython.display import display
from ipywidgets import interact


class TrieNode:
    def __init__(self):
        self.value = None
        self.children = {}
        self.is_word = False

    def suffixes(self):
        return self.suffixes_solver(suffix='', suffix_list=[])

    def suffixes_solver(self, suffix, suffix_list):
        if self.is_word:
            if suffix not in suffix_list:
                suffix_list.append(suffix)
        for child in self.children:
            temp_suffix = suffix + child
            node = self.children[child]
            node.suffixes_solver(temp_suffix, suffix_list)
        return suffix_list


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        curr_node = self.root
        for char in word:
            if char not in curr_node.children:
                curr_node.children[char] = TrieNode()
            curr_node = curr_node.children[char]
        curr_node.is_word = True

    def find(self, prefix):
        curr_node = self.root
        for char in prefix:
            if char not in curr_node.children:
                return False
            else:
                curr_node = curr_node.children[char]
        return curr_node


# testing

def f(prefix):
    if prefix != '':
        prefixNode = MyTrie.find(prefix)
        if prefixNode:
            print('\n'.join(prefixNode.suffixes()))
        else:
            print(prefix + " not found")
    else:
        print('')


MyTrie = Trie()
wordList = [
    "ant", "anthology", "antagonist", "antonym",
    "fun", "function", "factory",
    "trie", "trigger", "trigonometry", "tripod"
]
for word in wordList:
    MyTrie.insert(word)

interact(f, prefix='')
