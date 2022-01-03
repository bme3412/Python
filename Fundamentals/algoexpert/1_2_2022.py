# 1/2/2022
## did 3 problems:
    # validateSubsequence
    ## sortedSquaredArray
    ### TournamentWinner

### Key takeaways
    ## 1) don't be afraid to break the function and figure out why it doesn't work
    ## 2) most functions seem to start with instantiating the starting point, aka set the index of an array = 0 or = last value
    ## 3) start by figuring out what are the inputs and what to solve for
    ## 4) consider postive and negative integers

# validate Subsequence
# the prompt is: 
    # given 2 non-empty arrays of integers, write a function that determines whether array #2 is a subsequence of array #1
    #  a sub-sequence is an array of #s, that don't have to be adajacent; but appear in the same order as another array

# sample input:
array1 = [5, 1, 22, 25, 6, -1, 8, 10]
subsequence = [1, 6, -1, 10]

def validateSubsequence(array, sequence):
    arrIdx = 0
    seqIdx = 0
    while arrIdx < len(array) and seqIdx < len(sequence):
        if array[arrIdx] == sequence[seqIdx]:
            seqIdx +=1
        arrIdx +=1
    return seqIdx==len(sequence)

validateSubsequence(array1, subsequence)

## set the index for each array
# make sure the index of each array is less than the length of each array
    # aka, the index is not at the last position
# and then - if the value, as determine by calling the index position on the array = the value determined by calling the index position on the subsequence:
    # then increase the count of the index on the sub-sequence
# otherwise, go to the next position for the array
# and return True or False, depending on if the SeqIdx == the length of the sequence

# ------------------------------------------------------------ ##

## also did sortedSquareArray
### the goal is to write a function that squares the integers and sorts by highest value
#### the trick is to take into account the integers


# solution 1 -  brute force
def sortedSquaredArray(array):
    sortedSquares = [0 for _ in array]

    for idx in range(len(array)):
        value = array[idx]
        sortedSquares[idx] = value **2
    sortedSquares.sort()
    return sortedSquares

# solution 2 = more optimal - a bit more granular
# start by listing in array of all 0 values
# then set a pointer at index 0 and then the last position

def sortedSquareArray2(array):
    sortedSquares2 = [0 for _ in array]

    smallerValueIdx = 0
    largerValueIDx = len(array) - 1

    for idx in reversed(range(len(array))):
        smallerValue = array[smallerValueIdx]
        largerValue = array[largerValueIDx]

        if abs(smallerValue) > abs(largerValue):
            sortedSquares2[idx] = smallerValue **2
            smallerValueIdx +=1
        
        else:
            sortedSquares2[idx] = largerValue**2
            largerValueIDx -=1
    return sortedSquares2


# ------------------------------------------------------------ ##

## also did TournamentWinner

HOME_TEAM_WON = 1 # declare a constant

def tournamentWinner(competitions, results):
    currentBestTeam = "" # instantiate the best team
    scores = {currentBestTeam: 0}
    
    for idx, competition in enumerate(competitions):
        result = results[idx]
        homeTeam, awayTeam = competition # decompose to get separate values
        
        winningTeam = homeTeam if result == HOME_TEAM_WON else awayTeam # comapare to defined constant
         
        updateScores(winningTeam, 3, scores) # declare new function
        
        if scores[winningTeam] > scores[currentBestTeam]:
            currentBestTeam = winningTeam # update currentBestTeam 
    
    return currentBestTeam

def updateScores(team, points, scores): # checks to see if value declared; if not, instantiates and then adds points
    if team not in scores:
        scores[team] = 0
    scores[team] += points