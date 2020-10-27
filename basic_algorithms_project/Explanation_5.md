## Time Complexity

#### O(n)
The time complexity here is linear, because it is directly related to the number of letters stored in the trie. Since we are searching through the trie recursively, we encounter each node in the trie and then build our suffixes accordingly, all in linear time. Once we reach the end of each suffix, all we have to do then is return the output list of suffixes.


## Space Complexity

#### O(n)
Since our words are stored in the form of a trie, we can recursively search through all of the words without creating any additional data structures. Therefore, our trie requires O(n) space, where n represents the number of words (more precisely, the number of letters) added into our trie. The worst case scenario here is having no words with overlapping initial letters, so every word gets its own complete branch in the trie, but this scenario still only occupies O(n) space.

Additionally, the recursive function calls to determine the suffixes for each trie node require function calls on each successive letter of the word, resulting in a maximum potential space increase of 'n', which occurs when the suffixes solver is called on the root node of the Trie, and must list out all of the words in the trie. Otherwise, the number of recursions will be less than the number of nodes in the trie, since the nodes in the given prefix can be skipped.

## Code Design
At the heart of this code is a recursive trie traversal, which treats the trie branches like nodes in a tree and traverses them until it reaches the end of each word. However, finding suffixes requires us to store and keep track of each node that we visit behind the input prefix, so this requires the creation of a suffixes() function, which accumulates a suffix variable for each suffix traversed and also a suffix_list, which collects each of the suffixes that the recursion produces.
