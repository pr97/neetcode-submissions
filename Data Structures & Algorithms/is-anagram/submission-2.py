class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # nlogn
        # return sorted(s) == sorted(t)

        # n
        if len(s) != len(t):
            return False
        sm = {}
        tm = {}
        for x in s:
            sm[x] = sm[x] + 1 if x in sm else 1
        for x in t:
            tm[x] = tm[x] + 1 if x in tm else 1

        for x, c in sm.items():
            if tm.get(x) != c:
                return False

        return True

