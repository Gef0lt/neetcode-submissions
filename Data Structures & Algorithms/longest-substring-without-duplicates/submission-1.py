class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = []
        seen = set()
        max_len = 0

        for letter in s:
            if letter not in seen:
                queue.append(letter)
                seen.add(letter)
            else:
                max_len = max(max_len, len(seen))
                while queue[0] != letter:
                    last = queue.pop(0)
                    seen.remove(last)
                last = queue.pop(0)
                seen.remove(last)
                queue.append(letter)
                seen.add(letter)

        return max(max_len, len(seen))