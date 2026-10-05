class MedianFinder:

    def __init__(self):
        self.lower = []
        self.upper = []

    def addNum(self, num: int) -> None:
        # max heap
        heapq.heappush(self.lower, -num)
        max_item = -heapq.heappop(self.lower)
        heapq.heappush(self.upper, max_item)
        if len(self.lower) < len(self.upper):
            min_item = heapq.heappop(self.upper)
            heapq.heappush(self.lower, -min_item)

    def findMedian(self) -> float:
        if len(self.lower) > len(self.upper):
            return -self.lower[0]
        elif len(self.lower) == len(self.upper):
            l, r = -self.lower[0], self.upper[0]
            return (l+r)/2.0
        return 0.0
        