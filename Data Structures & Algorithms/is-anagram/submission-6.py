class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        frequency = [0] * 26

        for char in s:
            frequency[ord(char) - ord('a')] += 1

        for char in t:
            index = ord(char) - ord('a')
            frequency[index] -= 1

            if frequency[index] < 0:
                return False

        return True