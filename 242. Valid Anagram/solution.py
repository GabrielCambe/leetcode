class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters = {}
        # Iterate through the first string and count the characters        
        for char in s:
            letters[char] = letters.get(char, 0) + 1 
        
        # Iterate through the second string and decrement the count done earlier
        for char in t:
            # iI the char is not in the count, of if we have already decremented all the appearances, the string is not a valid anagram
            if char not in letters or letters[char] == 0:
                return False
            letters[char] -= 1
        
        # If we did not return on the loop, the string must be a valid anagram        
        return True
