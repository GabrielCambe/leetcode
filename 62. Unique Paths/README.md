# Solution
This problem is simple once you realize that the number of paths to any cell (i, j) is the sum of the paths to the cell above (i-1, j) and the cell to the left (i, j-1). This happens because our robot is limited to moving right or down. 
By realizing this, the problem can be solved using dynamic programming.


# Analysis
* Time: O(m * n), because we iterate through each cell of the m x n grid once to calculate the number of paths. The outer loop runs m-1 times and the inner loop runs n-1 times.

* Space: O(n), the array used to calculate the number of unique paths is of size n.


# Link
[leetcode](https://leetcode.com/problems/valid-anagram/description/)