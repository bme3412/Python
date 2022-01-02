# arrays =  a list in python
# ex: [1, 2, 3]
    # the operating system will transform all integers into binary format
# the # of memory slots linked to an array is fixed (if static); there is also dynamic arrays
    # static array - specify the length of array and in-memory of the array will have that length

## common operations
    # read a value at a given index 
        # accessing an array  at an elment runs in constant time
    # set and overwrite an element to an index:
        # need to locate at an index and then mutliplt the index by the # of memroy slots the object takes up - then overwrite the next x amount of fixed blocks
            # constant time O(1)
            # constant space  O(1)
    # initialize an array
        # constant time as n increases - the # of OS increases linearly with respect to n O(N) time and space
    # traversing an array (for loop)
        # the operating system traverse the memory slot
        # involves creating more memory blocks
        # O(n) time
        # O(1) space
    # map, reduce, fitler = O(n) time
    # insertion - inserting a value
        # pretty bad opertion
        # when insert have to copy the entire array/shift to the right (this comparable to traversing an array) = need to perform n operations
    # dynamic array can change in size
        # under the hood allows to have faster insertions at the end of the array
        # O(N) time complexity
        # constant time
        # popping is O(1) element space time
        





