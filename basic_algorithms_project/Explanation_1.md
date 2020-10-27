## Time Complexity

#### O(log(n))
By performing a binary search on all of the integers from zero to the given number, we are able to quickly find the square root. This binary search method yields a complexity of O(log(n)), where n represents the input number. This is ultimately far more efficient than the iterative solution to this problem, which has a worst-case scenario of O(n^1/2).


## Space Complexity

#### O(log(n))
The space complexity here actually winds up being the same as the time complexity. Even though no new data structures are created, the call stack expands every time we recursively call get_sqrt(), which will occur O(log(n)) times in the worst case scenario.


## Code Design
By treating the given number as the root element in a balanced binary tree, I could quickly navigate through this tree by dividing the possible number of solutions in half repeatedly through recursion. Since balanced, sorted binary trees can be navigated with respect to their height and our input number could be represented as a list of integers, I knew that this approach would yield the required time complexity of O(log(n)).
