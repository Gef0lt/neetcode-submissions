class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_len = 0

        for curr_letter in 'QWERTYUIOPASDFGHJKLZXCVBNM':
            l, r = 0, 0
            misses = k
            while r < len(s):
                if s[r] == curr_letter:
                    r += 1
                elif misses > 0:
                    misses -= 1
                    r += 1

                elif l >= r:
                    r += 1
                    l += 1
                else:
                    max_len = max(max_len, r - l)

                    if s[l] != curr_letter:
                        misses = min(misses + 1, k)
                    l += 1
            max_len = max(max_len, r - l)

        return max_len