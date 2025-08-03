# Solution
An inorder traversal is a traversal of a binary tree in which the left subtree is visited first, then the root node, and then the right subtree. This requires a stack to store the nodes. If you choose to do recursion, the stack is implicit, because the function call stack is used. If you choose to do iteration, you need to use an explicit stack.


# Analysis
Both have similar complexity, but there are different implications for the space complexity.

* Recursion:
  * Time: O(n) since we call the traverse function 1 time for each of the n nodes of the tree and the processing is an operation with constant time (printing).
  
  * Space: O(n) in the worst case (a skewed tree), since the number of calls in the stack will be n. Its O(log n) in the average case, since the maximum number of calls in the stack will be equal to the height of the tree.


* Iteration:
  * Time: O(n) since we have a loop that runs 1 time for each node in the tree and makes a constant time operation.
  
  * Space: O(n) in the worst case, because we would have a stack with n elements, in the average case, the numbers of element in the stack would be equal to the height of the tree.


# Link
[leetcode](https://leetcode.com/problems/binary-tree-inorder-traversal/)

