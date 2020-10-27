## Time Efficiency

#### O(N)
The efficiency here is determined by the length of the input string, therefore the time necessary for building the blockchain is linear, relative to the size of this string. Adding blocks to the chain requires the calculation of a new hash, the retrieval of the previous block's hash, the calculation of the timestamp, and the assignment of the value and previous block's next block. Fortunately, these actions all also take place in constant time, as we are simply appending the new block to the blockchain's tail.


## Space efficiency

#### O(N)
The creation of the blockchain is relative to the size of the input list, so our solution here requires a linear amount of space. Our output linked list is the same length of the input array, and the solution requires no other data structures to create the output.


## Code Design

The linked list is similar to a blockchain in many ways, and is therefore the data structure best suited for this solution. As mentioned above, setting up all of the pieces of the blocks prior to the creation of the chain helped to streamline the implementation of this function.
