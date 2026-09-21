class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = "".join(
            [x for x in s if (x >= "a" and x <= "z") or (x >= "0" and x <= "9")]
        )
        n = len(s)
        for idx in range(n >> 1):
            if not (s[idx] == s[n - idx - 1]):
                return False
        return True