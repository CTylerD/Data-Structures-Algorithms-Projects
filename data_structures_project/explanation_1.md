## Time efficiency

#### O(1)
By utilizing a hash table and an doubly linked list in this solution, we can regulate data in the cache in constant time. Using the hash table to store the nodes of the linked list allows us real-time access between the corresponding data in these two structures.


## Space efficiency

#### O(N)
The space complexity of this problem is derived from the LRU cache capacity. The length of the cache hash table and doubly linked list can never exceed this capacity, and since all operations occur in O(1) complexity, no additional space is necessary apart from these two data structures.


## Code Design

For efficiency reasons above, I chose to use a hash table to store the actual keys and values of the hash. However, since hash tables are inherently unordered, I utilized a doubly linked list for keeping track of the capacity and the access order of the LRU. This allows us to remove the least recently used item from the tail and add the most recently used item to the head, all in constant time.