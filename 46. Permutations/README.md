# Solution
You should use backtracking to solve this problem, basically, a backtrack auxiliar function is created, and it receives a possible permutation. IN the beggining of the function we validate the permutation, if it is valie (i.e the number of elements in the permutation is equal to the number of elements we have received to permutate) we save the new permutation and return. After that we come to the branching bit of the algorithm, where, in a loop, we generate a new possible permutation by appending every number that we did not use in the permutation to the current one.

# Analysis
* Time: O(n!). We call the auxiliary backtrack function n! times (where n == len(nums)), in each of these calls

* Space:


# Link
[leetcode](https://leetcode.com/problems/permutations/description/)