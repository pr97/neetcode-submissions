class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join(
            [x for x in s if (x >= "a" and x <= "z") or (x >= "A" and x <= "Z") or (x >= "0" and x <= "9")]
        )
        n = len(s)
        for idx in range(n >> 1):
            if not (s[idx].lower() == s[n - idx - 1].lower()):
                return False
        return True