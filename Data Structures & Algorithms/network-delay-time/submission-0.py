class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_map = {i:[] for i in range(n+1)}
        least_times = {node: float("inf") for node in range(1, n+1)}
        for l, r, w in times:
            adj_map[l].append((r,w))
        # BFS through the graph
        queue = deque([(k, 0)])
        least_times[k] = 0
        while queue:
            cur, time = queue.popleft()
            if least_times[cur] < time: 
                continue
            for n, w in adj_map[cur]:
                if time + w < least_times[n]:
                    least_times[n] = time + w
                    queue.append((n, time + w))
        res = max(least_times.values())
        return res if res < float('inf') else -1

        