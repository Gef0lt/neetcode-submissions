class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        ret = []

        for n in nums:
            counts[n] = counts.get(n, 0) + 1

        sorted_counts = sorted(counts.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            ret.append(sorted_counts[i][0])

        return ret