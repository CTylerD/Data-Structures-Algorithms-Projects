## Time Complexity

#### O(n log(n)))
The most complex operation we're performing here is the merge sort, which takes O(n log(n)) time to complete. Otherwise, we are just traversing through the sorted list once to create the output numbers, which takes linear time, and then outputting the results.


## Space Complexity

#### O(n)
Since merge sort recurses over exponentially smaller inputs each time it is called, the space complexity here is O(n), because even though the call stack is growing with each recursion, the space required by each successive call is half of the previous call. After the merge sort, we create two output strings which will hold all of the digits in the input list, so combined, they only require additional space of size n, the size of the input.


## Code Design
The two main steps to completing this problem were to sort the input list and generate the output numbers from this sorted list. I knew a merge sort would guarantee the required time complexity of O(n log(n)), and from there, I just appended the sorted numbers (in descending order) to two output strings, knowing that the number with the highest first digit would always be higher, whether the length of the input list was even or odd.
