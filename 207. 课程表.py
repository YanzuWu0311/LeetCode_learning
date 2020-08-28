"""
给定序列，判断课程先后顺序能否让学生修完这些课,只要课程不成环即可
拓扑排序，给定一个包含 n 个节点的有向图 G，我们给出它的节点编号的一种排列，如果满足：对于图 G 中的任意一条有向边 (u, v)，u 在排列中都出现在 v 的前面。
故不能有环存在。如果想要学习课程 A 之前必须完成课程 B，那么我们从 B 到 A 连接一条有向边。这样以来，在拓扑排序中，B 一定出现在 A 的前面。
方法一：深度优先搜索：假设我们当前搜索到了节点 u，如果它的所有相邻节点都已经搜索完成，那么这些节点都已经在栈中了，此时我们就可以把 u 入栈。
可以发现，如果我们从栈顶往栈底的顺序看，由于 u 处于栈顶的位置，那么 u 出现在所有 u 的相邻节点的前面。因此对于 u 这个节点而言，它是满足拓扑排序的要求的
方法二：广度优先搜索：删去没有入度的节点，同时该节点的出去的边也删除，重复到把整个图删了，这样内部有环的几个节点，永远删不掉
"""
import collections


# 深度优先
class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        edges = collections.defaultdict(list)
        # 在查询key报错时，可以提供默认值，不报错
        # 默认字典
        visited = [0] * numCourses
        # 是否访问过该节点
        # 0表示没有访问
        result = []
        valid = True
        # 表示这样排课是否可行

        for info in prerequisites:
            edges[info[1]].append(info[0])

        # 把prerequisites内容存储到edges中
        # info[1]指向info[0]

        def dfs(u):
            # 查看第u个节点
            # nonlocal声明的变量不是局部变量,也不是全局变量,而是外部嵌套函数内的变量。
            nonlocal valid
            # 可以继承上一层嵌套计算的valid
            visited[u] = 1
            # 正在遍历

            # 如果 v 为「未搜索」，那么我们开始搜索 v，待搜索完成回溯到 u；
            # 如果 v 为「搜索中」，那么我们就找到了图中的一个环，因此是不存在拓扑排序的；
            # 如果 v 为「已完成」，那么说明 v 已经在栈中了，而 u 还不在栈中，因此 u 无论何时入栈都不会影响到 (u, v) 之前的拓扑关系，以及不用进行任何操作。
            for v in edges[u]:
                if visited[v] == 0:
                    dfs(v)
                    if not valid:
                        return
                elif visited[v] == 1:
                    # 唯一返回Flase的原因是构成环
                    # 表明v又指回来，指向u
                    valid = False
                    return
            visited[u] = 2
            # 遍历完
            result.append(u)

        for i in range(numCourses):
            if valid and not visited[i]:
                # 遍历每一个节点，若valid还保持True，并且没被遍历过
                dfs(i)

        return valid, result


# 广度优先
class Solution1(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        edges = collections.defaultdict(list)
        indeg = [0] * numCourses
        # 记录入度
        for info in prerequisites:
            edges[info[1]].append(info[0])
            indeg[info[0]] += 1
        q = collections.deque([u for u in range(numCourses) if indeg[u] == 0])
        # 搜集所有入度为0的节点
        visited = 0
        while q:
            visited += 1
            u = q.popleft()
            # 删去入度为0的点
            for v in edges[u]:
                # 对于即将删去的入度为0的节点
                # 遍历从他这出去的边连接的节点
                # 把这些节点的入度减一
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
                    # 若这些节点的入度也为0
                    # 加入队列
        return visited == numCourses


num = 5
pre = [[1, 0], [4, 3], [2, 1], [3, 2], [3, 4]]
Solution_canFinish = Solution1()
print(Solution_canFinish.canFinish(num, pre))
