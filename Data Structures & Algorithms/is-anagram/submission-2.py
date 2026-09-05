class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        set1 = list(s)
        set1.sort()
        set2 = list(t)
        set2.sort()
        if set1 == set2:
            return True
        return False
        