class Solution:
    def __init__(self):
        # Define a auxiliar array to save the result, it is acessible to every method call we are going to make
        self.traversal = []
    
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if (root):
            # Traverse to the leftmost child
            if (root.left):
                self.inorderTraversal(root.left)

            # Process current node
            self.traversal.append(root.val)

            # Traverse left
            if (root.right):
                self.inorderTraversal(root.right)

        return self.traversal
