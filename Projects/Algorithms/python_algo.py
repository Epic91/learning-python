# Algorithm for palindrome

str = ' racecar'

# Step 1: check if the value at index 0 is equal to the value of the last index
# Step 2: Check if the first index and last index are not the same, if not return false and they are return True

def isPalindrome(str):
    startIndex = 0
    endIndex = len(str) - 1

    for x in str:
        if str[startIndex] != str[endIndex]:
            return False
    return True 