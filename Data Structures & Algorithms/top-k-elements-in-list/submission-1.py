from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_map = Counter(nums) # [1:1, 2:2, 3:3] number:count
        return heapq.nlargest(k, count_map.keys(), key = count_map.get )


        