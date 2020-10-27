## Time Efficiency

#### O(N)
The complexity for determining the union is linear, due to the repeated iteration over the linked lists containing the set data.

By utilizing auxiliary sets, linear time complexity is also achievable for the intersection solution, since checking to see if a given item is in a set happens in constant time. By utilizing the set data structure, we are able to avoid any further complexities that might arise from attempting to manipulate linked lists on their own.


## Space efficiency

#### O(N)
The space complexity here is relative to the size of the input linked lists. Though we are creating several other data structures in this solution, they are always relative to and never exceed the combined size of our in initial inputs. Therefore, in the worst-case scenarios (two lists with no intersecting elements or two identical sets), the space complexity is still only linear.


## Code Design

For each of these solutions, I took advantage of the set data structure, since it has the property of not containing any duplicate data values. Thus, being able to search for elements in constant time allowed me to complete the intersection function linearly, rather than quadratic time.