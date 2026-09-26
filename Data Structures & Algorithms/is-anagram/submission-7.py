class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequency = [0] * 26
        base = ord('a')

        for char in s:
            frequency[ord(char) - base] += 1

        for char in t:
            index = ord(char) - base
            frequency[index] -= 1

            if frequency[index] < 0:
                return False

        return True