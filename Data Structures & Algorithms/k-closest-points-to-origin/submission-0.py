class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for x, y in points:
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(max_heap, (-distance, x, y))
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        return list((x, y) for _, x, y in max_heap)