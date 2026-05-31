class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = deque()
        res.append([])

        for n in nums:
            for i in range(len(res)):
                a = res.popleft()
                b = a.copy()
                b.append(n)
                res.append(a)
                res.append(b)

        return list(res)
        