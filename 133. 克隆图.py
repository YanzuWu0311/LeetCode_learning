"""
把原图进行深复制，只能复制节点val，不能直接复制节点的邻居列表
深度优先，遍历已知节点的所有邻居，分别创建克隆点，每个克隆点也要创建其邻居列表，用字典存储原图节点到克隆节点的映射
"""


# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=None):
        if neighbors is None:
            neighbors = []
        self.val = val
        self.neighbors = neighbors


class Solution(object):

    def __init__(self):
        # 原图中的点：新建的克隆点
        self.visited = {}

    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        if not node:
            return node

        # 如果该节点已经被访问过了，则直接从哈希表中取出对应的克隆节点返回
        if node in self.visited:
            return self.visited[node]

        # 克隆节点，注意到为了深拷贝我们不会克隆它的邻居的列表
        clone_node = Node(node.val, [])

        # 哈希表存储
        self.visited[node] = clone_node

        # 遍历该节点的邻居并更新克隆节点的邻居列表
        if node.neighbors:
            clone_node.neighbors = [self.cloneGraph(n) for n in node.neighbors]

        return clone_node
