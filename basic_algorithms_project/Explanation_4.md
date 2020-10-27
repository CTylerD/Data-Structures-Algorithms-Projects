## Time Complexity

#### O(n)
Since this problem can be solved with a single traversal of the input, the worst case time complexity is O(n), which occurs anytime there isn't a two in the array. The best case scenario actually operates in constant time, but this only occurs if the entire array is comprised of twos.


## Space Complexity

#### O(n)
Since no new data structures or recursive calls are made here, the only space required is that occupied by the original input. Otherwise, the indices move through this array, sorting everything in place until the array is completely sorted.


## Code Design
Since there are only three distinct elements in this array, I knew it would be possible to use indices on either end as a sort of buffer, to show where zeros and twos have already been correctly sorted. Since it isn't possible to move any digits behind these indices, once the zeros and twos were properly sorted, it can be assumed that the ones remain in the middle. Even in scenarios where there are only one or two unique digits in the input array, the same logic holds true.
