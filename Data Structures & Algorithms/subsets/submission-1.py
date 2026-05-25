class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        q = deque()
        q.append([])

        for el in nums:
            for i in range(len(q)):
                a = q.popleft()
                b = a.copy()
                a.append(el)
                q.append(a)
                q.append(b)

        return list(q)
        