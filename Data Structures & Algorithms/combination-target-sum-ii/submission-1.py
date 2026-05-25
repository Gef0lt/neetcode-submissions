class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        hashmap = {}
        for el in candidates:
            if el in hashmap:
                hashmap[el] += 1
            else:
                hashmap[el] = 1

        q = deque()
        q.append([[], 0])
        ans = []

        for val, counter in hashmap.items():
            for i in range(len(q)):
                a, total = q.popleft()

                for j in range(counter + 1):
                    new_total = total + val * j
                    if new_total > target:
                        break
                    elif new_total == target:
                        ans.append(a.copy() + [val] * j)
                        break
                    q.append([a.copy() + [val] * j, new_total])


        return ans