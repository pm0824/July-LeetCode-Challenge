'''
Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
'''

#Solution:

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        if not inorder or not postorder:
            return None
        
        val = postorder.pop()
        root = TreeNode(val)
        
        index = inorder.index(val)
        
        right_branch = inorder[index+1:]
        left_branch = inorder[:index]
        
        root.right = self.buildTree(right_branch, postorder)
        root.left = self.buildTree(left_branch, postorder)
            
        return root
        
        
        
        
