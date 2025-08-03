class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        traversal = []

        if root == None:
            return traversal
        
        stack = []
        current_node = root

        while len(stack) > 0 or current_node:
            # Traverse to the leftmost child
            while current_node:
                stack.append(current_node)
                current_node = current_node.left
            
            current_node = stack.pop()

            # Process the current node
            traversal.append(current_node.val)

            # Traverse tp the right child
            current_node = current_node.right
        
        return traversal
