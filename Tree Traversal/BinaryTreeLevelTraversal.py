
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        result, level = [], [root]
        while level:
            result.append([node.val for node in level])
            tmp = []
            for node in level:
                tmp.extend([node.left, node.right])
            level = [node for node in tmp if node] # level = tmp nope! as None does not have 'val'
        return result
    
#     3
#    / \
#   9  20
#     /  \
#    15   7

t = TreeNode(3)
t1 = TreeNode(9)
t2 = TreeNode(20)
t.left = t1
t.right = t2
t3 = TreeNode(15)
t4 = TreeNode(7)
t2.left = t3
t2.right = t4

print(t.levelOrder(t))

#[[3], [9, 20], [15, 7]]