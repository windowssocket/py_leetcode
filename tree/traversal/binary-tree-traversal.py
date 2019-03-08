# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# cxd
class Solution(object):

    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = [[]for _ in range(self.getHeight(root))]
        self.traversal(root, 0, ret)
        return ret

    def getHeight(self, root):
        if root is None:
            return 0
        left = self.getHeight(root.left)
        right = self.getHeight(root.right)
        return max(left, right) + 1

    def traversal(self, root, level, ret):
        if root is None:
            return
        ret[level].append(root.val)
        self.traversal(root.left, level+1, ret)
        self.traversal(root.right, level+1, ret)
# lmf
# dfs 因为不再需要多次拷贝，有空间优化
class Solution:
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        Solution.res = []
        def dfs(root,depth):
            if not root:
                return
            if depth <= len(Solution.res) - 1:
                Solution.res[depth].append(root.val)
            else:
                Solution.res.append([root.val])
            dfs(root.left, depth+1)
            dfs(root.right, depth+1)
        dfs(root,0)
        return Solution.res
# bfs
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        res = []
        if not root:
            return res
        queue = [root]
        while queue:
            length = len(queue)
            tmpList = []
            for i in range(length):
                node = queue.pop(0)
                tmpList.append(node.val)
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            res.append(tmpList)
        return res



