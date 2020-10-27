class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __repr__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None

    def __str__(self):
        cur_head = self.head
        out_string = ""
        while cur_head:
            out_string += str(cur_head.value) + " -> "
            cur_head = cur_head.next
        return out_string

    def append(self, value):
        if self.head is None:
            self.head = Node(value)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(value)

    def pop(self):
        if self.head is None:
            return None
        node = self.head
        self.head = self.head.next
        return node

    def size(self):
        size = 0
        node = self.head
        while node:
            size += 1
            node = node.next
        return size


### Solution without using sets

def union(llist_1, llist_2):
    output = LinkedList()
    union_tracker = []
    ll1_curr = llist_1.head
    ll2_curr = llist_2.head
    while ll1_curr:
        if ll1_curr.value not in union_tracker:
            union_tracker.append(ll1_curr.value)
            output.append(ll1_curr)
        ll1_curr = ll1_curr.next
    while ll2_curr:
        if ll2_curr.value not in union_tracker:
            union_tracker.append(ll2_curr.value)
            output.append(ll2_curr)
        ll2_curr = ll2_curr.next
    return output


def intersection(llist_1, llist_2):
    output = LinkedList()
    ll1_curr = llist_1.head
    ll2_curr = llist_2.head
    while ll1_curr.next:
        while ll2_curr.next:
            if ll1_curr.value == ll2_curr.value:
                output.append(ll2_curr)
            else:
                ll2_curr = ll2_curr.next
        ll1_curr = ll1_curr.next
        ll2_curr = llist_2.head
    return output



# Union test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]
solution = [1, 2, 3, 4, 6, 9, 11, 21, 32, 35, 65]

for i in element_1:
    linked_list_1.append(i)

for j in element_2:
    linked_list_2.append(j)

output = union(linked_list_1, linked_list_2)
output_list = []
while output.head:
    output_list.append(output.pop().value)
if output_list == sorted(solution):
    print("Test case 1 union: Pass!")
else:
    print("Test case 1 union: FAIL.")


# Intersection test case 1

linked_list_1 = LinkedList()
linked_list_2 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,21]
element_2 = [6,32,4,9,6,1,11,21,1]
solution = [4, 6, 21]

for i in element_1:
    linked_list_1.append(i)

for j in element_2:
    linked_list_2.append(j)

output = intersection(linked_list_1, linked_list_2)
output_list = []
while output.head:
    num = output.pop().value
    output_list.append(num)
print(output_list)
if sorted(output_list) == solution:
    print("Test case 1 intersection: Pass!")
else:
    print("Test case 1 intersection: FAIL.")


# Union test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]
solution = [1, 2, 3, 4, 6, 7, 8, 9, 11, 21, 23, 35, 65]

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

output = union(linked_list_3, linked_list_4)
output_list = []
while output.head:
    output_list.append(output.pop().value)
if sorted(output_list) == solution:
    print("Test case 2 union: Pass!")
else:
    print("Test case 2 union: FAIL.")


# Intersection test case 2

linked_list_3 = LinkedList()
linked_list_4 = LinkedList()

element_1 = [3,2,4,35,6,65,6,4,3,23]
element_2 = [1,7,8,9,11,21,1]
solution = []

for i in element_1:
    linked_list_3.append(i)

for i in element_2:
    linked_list_4.append(i)

output = intersection(linked_list_1, linked_list_2)
output_list = []
while output.head:
    output_list.append(output.pop().value)
if sorted(output_list) == solution:
    print("Test case 2 intersection: Pass!")
else:
    print("Test case 2 intersection: FAIL.")
