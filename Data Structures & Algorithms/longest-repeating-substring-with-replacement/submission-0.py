class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        for c in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            count[c] = 0
        count[s[0]] = 1
        l = 0
        r = 1
        max_len = k
        while r < len(s):
            while count[max(count, key = count.get)] + k >= r - l and r < len(s):
                
                count[s[r]] += 1
                if max_len < r - l:
                    max_len = r - l
                r += 1
            while count[max(count, key = count.get)] + k < r - l and l < r:
                count[s[l]] -= 1
                if count[s[l]] == -1:
                    count[s[l]] = 0
                l += 1
        if r - l > max_len:
            max_len = r - l
            
        return max_len
            