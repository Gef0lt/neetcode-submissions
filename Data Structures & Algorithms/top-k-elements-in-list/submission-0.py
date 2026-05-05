class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dic = {}
        for el in nums:
            if el in dic:
                dic[el] += 1
            else:
                dic[el] = 1

        sDict = sorted(dic.items(), key=lambda x: x[1], reverse = True)
        ans = []
        for i in range(k):
            ans.append(sDict[i][0])
        
        return ans