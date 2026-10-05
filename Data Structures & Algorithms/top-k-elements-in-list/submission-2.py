class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_freq = Counter(nums)
        l = len(num_freq)
        if l <= k: return [item[0] for item in num_freq.items()]
        heap = []
        for i, (num, freq) in enumerate(num_freq.items()):
            if i < k:
                heapq.heappush(heap, (freq, num))
            elif freq > heap[0][0]:
                heapq.heapreplace(heap, (freq, num))
        return [k for v, k in heap]