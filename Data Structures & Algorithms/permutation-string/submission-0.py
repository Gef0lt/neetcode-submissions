class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0
        r = len(s1) - 1
        s1_hash = {}
        s2_hash = {}
        for c in 'qwertyuiopasdfghjklzxcvbnm':
            s1_hash[c] = 0
            s2_hash[c] = 0

        for c in s1:
            s1_hash[c] += 1

        for c in s2[:len(s1)]:
            s2_hash[c] += 1
            
        if s1_hash == s2_hash:
                return True

        r += 1

        while r < len(s2):
            s2_hash[s2[r]] += 1
            s2_hash[s2[l]] -= 1

            if s1_hash == s2_hash:
                return True
            l += 1
            r += 1

        return False
            
            
