## Time Complexity


#### O(n))
Traversing the router to find a given handler is potentially an extremely efficient process, since we are only searching for a single handler at any one time. Since the storage trie in the router can be treated like a tree with many overlapping branches, even if the router stored millions of pathways, we would be able to locate the handler for any one of them in an amount of time relative to the length of the handler. The worst case scenario here is when the trie only has a single pathway stored in it and we are required to traverse the entire trie. Since our trie cannot be balanced and any node can have any number of children, we can't assume anything further about the time complexity that we might about other types of trees. However, since the maximum distance we ever have to travel is the height of the tree, it can still be assumed that this is an efficient solution


## Space Complexity

#### O(n)
The space complexity here is comprised of the total number of path components and handlers stored in the router. Traversing the router trie to search for the requested handler doesn't require any new space, so the only space required is that of the router itself and the pathways and handlers that it contains.



## Code Design
The router is implemented by inserting each part of a given pathway as a node in the trie. That way, these parts can later be re-assembled by joining them with forward slashes, to re-form the pathway. We've used "is_word" to denote the end of a word on dictionary-type applications of the trie, so similarly, we can insert the handler in the final node of each pathway, which will alert us that we've reached the end of the requested path and return the appropriate handler.
