## Time Complexity

#### O(log(n))
Similar to the previous problem, the fastest way to deal with a sorted list is to recursively search through it like it were a binary tree. Since the list was completely sorted, apart from the point of rotation, we could compare our result to the sorted half and proceed through the recursion. The iterative solution requires O(N) time to search through the entire list, so this winds up being far more efficient.


## Space Complexity

#### O(n log(n))
Again, this problem requires the creation of no new data structures, since we're searching for an element in a list. However, the recursive function calls do add up in the call stack, which will ultimately require O(log(n)) space. This recursion is also relative to the size of the input list, 'n', which requires O(n) space to store.


## Code Design
Even though there was a single point of rotation, since the provided list was otherwise sorted, I knew that at least one of the two halves would be properly sorted. After comparing the given number to this half, I could then chose the half that contained the number and continue the binary search, recursing through this process until either the number was found, or I ran out of numbers.
