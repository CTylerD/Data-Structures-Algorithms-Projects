## Time Complexity

#### O(n)
The get_min_max function operates in linear time, as it only requires one traversal through the input list to determine the correct min and max.


## Space Complexity

#### O(n)
This function requires no additional space beyond the input , and therefore, only occupies however much space is required by the initial array.


## Code Design
By having separate variables for the min and max value, we can traverse the array in linear time and compare these variables to the current element, updating as we go, until we reach the end of the array. In this way, we can find the requested values in a single traversal, through comparisons at each index.
