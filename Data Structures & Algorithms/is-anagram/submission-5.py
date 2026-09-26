class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        frequency = {}
        for char in s:
            if char not in frequency:
                frequency[char] = 1
            else:
                frequency[char] += 1
        for char in t:
            if char not in frequency:
                return False
            frequency[char] -= 1
            if frequency[char] < 0:
                return False
        return True