# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:        
        def dfs(root):
            if not root:
                return "#"
            
            return (
                "," + str(root.val) +
                dfs(root.right) +
                dfs(root.left)
            )

        return dfs(subRoot) in dfs(root) 