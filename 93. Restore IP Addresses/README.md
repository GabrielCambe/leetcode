# Solution
For this problem i used backtracking, starting from an empty string, the algorithm generates all possible valid parts, line 48 is the most important, after the recursion, i remove the last part added to the adress to that in the next iteration of the branching loop, the algorithm chooses another possible part. This ensures that all possible valid IP adresses will be found.


# Analysis
* Time: O(1), the algorithm runs in constant time. The string size n has bounds (4 <= n <= 12) and the branching also has (+3 resursions per call). As the ip adresses have a maximum of 4 parts, we have a constant call depth for this algorithm and as we increase the size n of the string, the function will discard the input and just return an empty array. 

* Space: O(1), as we have a maximum call depth of 4 and the number of possible ip adresses for the string of bounded size n is finite.


# Link
[leetcode](https://leetcode.com/problems/restore-ip-addresses/)