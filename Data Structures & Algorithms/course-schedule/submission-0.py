class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i:[] for i in range(numCourses)}
        indegrees = [0] * numCourses
        for course, pre in prerequisites:
            preMap[pre].append(course)
            indegrees[course] += 1
        queue = deque([i for i in range(numCourses) if indegrees[i] == 0])
        order = []
        while queue:
            cur = queue.popleft()
            order.append(cur)
            for neighbor in preMap[cur]:
                indegrees[neighbor] -= 1
                if indegrees[neighbor] == 0:
                    queue.append(neighbor)
        return len(order) == numCourses