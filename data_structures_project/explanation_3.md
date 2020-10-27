## Time Efficiency

### Encoding:

#### O(n log n)
The least time efficient parts of this solution are sorting the list of tuples by frequency and sorting the list of nodes after building the tree. Otherwise, most of the solution takes place in linear time, respective to the size of the length of the input string or the size of the derived Huffman tree.

### Decoding

#### O(N)
By traversing the tree in tandem with the encoded data, we are able to decode the string in linear time. This decoding solution also handles the case where our entire string is comprised of a single character and therefore, our tree is only a single node.



## Space Efficiency

### Encoding:

#### O(N)
Since all data in this problem is derived from the initial argument, our space complexity here is linear. Even though multiple data structures are created and iterated through during the course of this program, they are all related to the number of unique characters in the input string.

### Decoding:

#### O(N)
The space required to store the encoded data is considerably less than that of the input string, despite requiring several data structures to reach that space optimization. The decoding process makes use of the tree structure to traverse the tree and build the decoded string, so the space complexity required here is the same as the encoding process, since they utilize the same data structures. The only new space we occupy is that of the rebuilt string.


## Code Design

For the design of this problem, I broke the solution into many phases and built towards the encoding/decoding process. Once I was able to successfully build an accurate Huffman tree, the encoding and decoding functions came together easily. By creating the frequency dictionary before building the tree and then creating the tree before assigning the binary values, I was able to create more straightforward solutions, rather than trying to tackle too many problems at the same time. Utilizing node objects in the form of a tree structure was the best way to keep track of data, however, a hash table was also necessary for determining the relative frequencies of the characters in the initial string. This table provided the values for the array of tuples that were ultimately used to create these nodes.
