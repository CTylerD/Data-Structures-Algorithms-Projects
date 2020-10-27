## Time Efficiency

#### O(N)
The complexity here is relative to the number of groups, sub-groups, and users. Similar to problem two, traversing each group and sub-group is necessary for determining whether or not the requested user is present in these groups, so our complexity must be linear.


## Space efficiency

#### O(U + G)
The worst case scenario would require visiting (G) number of directories while searching for (U) number of users. This means that our worst case output file would contain all users (U) and the most number of directories we would need to traverse is (U). After reducing (2U + 2G), we are left with O(U + G).


## Code Design

Here, I chose to use a recursive approach, since the task performed on each group is identical to the one performed on each sub-group. The underlying data structure of the group/sub-group structure is a tree, so we can efficiently traverse this tree through recursion. Assigning the various groups and users contained within each group object to arrays was the best way of keeping track of these for ease of access and potential alteration.
