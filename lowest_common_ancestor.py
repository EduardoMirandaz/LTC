# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':

        p_ancestors = [root]
        q_ancestors = [root]
        
        root_save = root

        while root.val != p.val:
            p_ancestors.append(root)
            if(p.val > root.val):
                root = root.right
            elif(p.val < root.val):
                root = root.left
        else:
            p_ancestors.append(root)


        while root_save.val != q.val:
            q_ancestors.append(root_save)            
            if(q.val > root_save.val):
                root_save = root_save.right
            elif(q.val < root_save.val):
                root_save = root_save.left
        else:
            q_ancestors.append(root_save)


        idx = 0

        q_ancestors_size = len(q_ancestors)
        p_ancestors_size = len(p_ancestors)

        if p_ancestors_size > q_ancestors_size:
            idx = q_ancestors_size - 1
        else:
            idx = p_ancestors_size - 1
        
        while q_ancestors[idx] != p_ancestors[idx]:
            idx-=1
        
        return q_ancestors[idx]



# other solution


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        elif p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root