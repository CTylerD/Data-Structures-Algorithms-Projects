## Time Efficiency

#### O(N)
Because this solution only looks and every file and folder once, the complexity increases linearly with the size of the directory tree. Since this problem requires examining each file name, this direct path is the most efficient way of finding the requested files.


## Space efficiency

#### O(F + D)
The space occupied by this problem is relative to the size of the directory tree, which is comprised of some number of directories (D) and some number of files (F). In addition to the space the tree occupies, we must also consider the space required for the call stack, which is relative to the number of directories (D). Additionally, our output list of desired files also occupies some amount of space, relative to the number of target files found in the directory tree (F)

The worst case scenario for traversing our directory tree is the full size of the directory structure (D), and the worst case scenario for the size of the call stack occurs when our directory tree contains only directories and no files, meaning that the number of calls in the stack is equal to the size of the directory structure. Therefore, when taking everything into account, the total efficiency becomes O(F + D + F + D), which reduces to O(F + D).

## Code Design

Since the program is looking at each file in a given directory and venturing into each of the directory's sub-directories to perform a similar task, I chose to use a recursive approach. Since we're only interested in the paths of these directories, I chose to store these in an array, for easy access and amendment.
