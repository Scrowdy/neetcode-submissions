# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        largest_dia = [0]

        def height(root):
            if root is None:
                return 0
            
            left_h = height(root.left)
            right_h = height(root.right)
            diameter = left_h + right_h

            largest_dia[0] = max(largest_dia[0],diameter)

            return 1+ max(left_h,right_h)

        height(root)
        return largest_dia[0]