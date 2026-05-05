class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = {}
        ret = []

        for s in strs:
            val = ''.join(sorted(s))
            if val in anagrams:
                anagrams[val].append(s)
            else:
                anagrams[val] = [s]

        for k, v in anagrams.items():
            ret.append(v)

        return ret