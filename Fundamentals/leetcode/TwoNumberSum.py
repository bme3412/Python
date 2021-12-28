#### Prompt: #####
    # write a function that:
        # takes in a non-empty array of Distinct integers;
        # and an integer == to a target sum
    # if any 2 #s in the Distinct Input array sum to the taret sum => the function should return the integers in an array
    # if no 2 #s in the Array sum to the target sum, the function should return an empty array
    # cannot add a single integer to itself to obtain the target sum
    # there will be at most, 1 pair of #s that sum to the target sum

def twoNumberSum(array, targetSum):
    # code
    pass

# example:
    # array = [3, 5, -4, 8, 11, 1, -1, 6]
    # targetSum = 10

    # the goal is to find if there are 2 #s in array, that sum to 10 (targetSum)

###### Conceptual ######
# 1) Two For loops could work to traverse the array
    # but this not optimal as it will take O(n**2) for 2 for loops

# 2) So could use a hash table 
    # will take up more space
    # but to reduce time
        # use a python dictionary
        ## ex:
            ###   if targetSum = 10
            ### currentNum = x
            ### find #y, where x + y = 10; or, y = 10 - x
    # time compleixty = O(N) where n = length of array
    # space complexity = O(N) b/c adding balues to hash table
        
##### Coding ######

# 2 For loops:
def twoNumberSum(array, targetSum):
    for i in range(len(array-1)):
        firstNum = array[i]
        for j in range(i +1, len(array)):
            secondNum = array[j]
            if firstNum + secondNum == targetSum:
                return [firstNum, secondNum]
    return []

## Big O notation:
    ## O(n**2) time
    ## O(1) space

## Hash Table
def twoNumberSum(array, targetSum):
    nums = {}  # delare an empty hash table/dictionary
    for num in array:
        if targetSum-num in nums:
            return [targetSum-num, num]
        else:
            nums[num]= True ## store in hash
    return []

## Big O Notation
    ## O(n) time
    ## O(n) space