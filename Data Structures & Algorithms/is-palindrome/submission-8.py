class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleans = ""
        for letter in s:
            if letter.isalpha() or letter.isdigit():
                cleans += letter.lower()

        return cleans == cleans[::-1]