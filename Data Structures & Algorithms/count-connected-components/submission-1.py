class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_map = {i:[] for i in range(n)}
        for l, r in edges:
            adj_map[l].append(r)
            adj_map[r].append(l)
        unvisited = set(range(n))
        count = 0
        while unvisited:
            item = min(unvisited)
            queue = deque([item])
            while queue:
                cur = queue.popleft()
                unvisited.discard(cur)
                for neighbor in adj_map[cur]:
                    if neighbor in unvisited:
                        queue.append(neighbor)
            count += 1
        return count
