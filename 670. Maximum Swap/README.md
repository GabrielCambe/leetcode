# Solution
To find the solution, whe need to look into each of the digits and find the optimal swap. This will be swapping the first number from the left that is smaller from the rightmost occurence of a number. The algorithm does that

# Analysis
* Time: O(n), where n is the number of digits of the input. The first operation is to separate the digits of the number, the process takes O(n) time plus O(n) time to reverse the digits array. After that, we need O(n) time to build a dictionary with the index of the last occurrence of each digit. After that we have a lopp that runs n times, and for each, we perform a search for the last_occurrence of such digit, this search has O(1) time amortized, as it is made in a hash table, but have O(n) time in the case of cache collisions, but as we only use digits as keys, this shouldnt happen. So for the searching we have O(n) * O(1). When we find the optimal swap, we need to create the number again, and this takes O(n) time.
In the end we have 4 * O(n) which is O(n).

* Space: O(n) also. We have the digits array of size n and the last_ocurrence dictionary, that also has at most n elements on it. 


# Link
[leetcode](https://leetcode.com/problems/maximum-swap/description/)