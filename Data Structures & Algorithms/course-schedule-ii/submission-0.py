class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        indegrees = [0] * numCourses
        for c, pre in prerequisites:
            preMap[pre].append(c)
            indegrees[c] += 1
        visited = []
        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
        while queue:
            cur = queue.popleft()
            visited.append(cur)
            for postreq in preMap[cur]:
                indegrees[postreq] -= 1
                if indegrees[postreq] <= 0:
                    queue.append(postreq)
        if len(visited) == numCourses:
            return visited
        else:
            return []