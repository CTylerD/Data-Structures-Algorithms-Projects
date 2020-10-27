class LRU_Cache():

    def __init__(self, capacity):
        self.size = 0
        self.capacity = capacity
        self.cache = {}
        self.llist = Doubly_Linked_List()  # tail is LRU

    def get(self, key):
        if self.cache.get(key):
            new_node = self.cache[key]
            if new_node != self.llist.head:
                self.llist.remove(key)
                self.llist.prepend(key, self.cache[key].value)
            return self.llist.head.value
        else:
            return None

    def set(self, key, value):
        if self.capacity == 0:
            return None
        if self.is_full():
            self.cache.pop(self.llist.tail.key, -1)
            self.llist.tail = self.llist.tail.prev
            self.llist.tail.next = None
            self.size -= 1
        new_node = DoubleNode(key, value)
        self.cache[key] = new_node
        self.llist.prepend(key, value)
        self.size += 1

    def is_full(self):
        return self.size == self.capacity


class DoubleNode():

    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class Doubly_Linked_List():

    def __init__(self):
        self.head = None
        self.tail = None

    def prepend(self, key, value):
        if self.head is None:
            self.head = DoubleNode(key, value)
            self.tail = self.head
            return
        if key == self.tail.key:
            self.tail = self.tail.prev
        new_head = DoubleNode(key, value)
        new_head.next = self.head
        self.head.prev = new_head
        self.head = new_head

    def remove(self, key):
        if self.head is None:
            return
        if self.head.key == key:
            self.head = self.head.next
            return
        node = self.head
        while node.next:
            if node.next.key == key:
                node.next = node.next.next
                return
            node = node.next
        raise ValueError("Value not found in the list.")


# test case 1 - append and regulate cache relative to capacity
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
while True:
    if our_cache.get(1) != 1 or\
       our_cache.get(2) != 2 or\
       our_cache.get(9) != None:
        print("Test case 1: FAIL.")
        break
    our_cache.set(5, 5)
    our_cache.set(6, 6)
    if our_cache.get(3) == None and our_cache.is_full() is True:
        print("Test case 1: Pass!")
        break
    else:
        print("Test case 1: FAIL.")
        break


# test case 2 - zero capacity cache
our_cache = LRU_Cache(0)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.get(2)
our_cache.get(3)
if our_cache.get(1) is None and\
   our_cache.get(2) is None and\
   our_cache.is_full() is True:
    print("Test case 2: Pass!")
else:
    print("Test case 2: FAIL.")


# test case 3 - replacing key with new value
our_cache = LRU_Cache(5)
our_cache.set(1, 1)
our_cache.set(2, 2)
our_cache.set(3, 3)
our_cache.set(4, 4)
our_cache.set(2, 5)
if our_cache.get(2) != 5:
    print("Test case 3: FAIL.")
else:
    print("Test case 3: Pass!")
