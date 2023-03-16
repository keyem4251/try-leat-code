#
# @lc app=leetcode id=94 lang=python3
#
# [94] Binary Tree Inorder Traversal
#
from typing import Optional, List

# @lc code=start
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        
        if root is None:
            return result

        node = root
        parent = None

        while True:
            if node is None:
                break

            if node.left is None:
                result.append(node.val)
                if node.val == parent.right.val:
                    node = parent
                elif parent.right is not None:
                    node = parent.right
            else:
                parent = node
                node = node.left

        return result
# @lc code=end

