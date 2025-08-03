# Solution
The solution consists in counting the frequency of the characters in the first string, and then iterating through the second string and checking if it is the same frequency.


# Analysis
* Time: O(n), we iterate throught both of the arrays once, so we have O(n) + O(n) = O(n). It is important 

* Space: O(1), the algorithm uses a python dict to store the frequency of characters. As the strings consist only of lowercase English letters. This means the maximum number of keys in the dict is 26. Because the size is capped by a constant (26), the space complexity is considered constant space.


# Link
[leetcode](https://leetcode.com/problems/unique-paths/description/)