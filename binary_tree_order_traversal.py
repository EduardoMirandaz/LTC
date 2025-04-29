# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        levels_queue = [root]
        ans = [[root.val]]
        while levels_queue:
            actual = levels_queue.pop(0)
            level_list = []
            if actual.left:
                levels_queue.append(actual.left)
                level_list.append(actual.left.val)
            if actual.right:
                levels_queue.append(actual.right)
                level_list.append(actual.right.val)
            if(level_list):
                ans.append(level_list)
        return ans


import collections
import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        
        q = collections.deque()
        q.append(root)

        res = []

        while q:
            q_len = len(q)
            actual_level = []
            for i in range(q_len):
                node = q.popleft()
                if node:
                    actual_level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if(actual_level):
                res.append(actual_level)

        return res