# # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
            
    def pathSum(self, root, targetSum):
        
        self.ans = []
        
        def dfs(node, sum, current_path):

            tmp = current_path+[node.val]
            sum = sum + node.val

            if(node.right):
                dfs(node.right, sum, tmp)
            if(node.left):
                dfs(node.left, sum, tmp)
            
            if(node.left == None and node.right == None):
                if(sum == targetSum):
                    self.ans.append(tmp)

        
        dfs(root, 0, [])
        return self.ans

