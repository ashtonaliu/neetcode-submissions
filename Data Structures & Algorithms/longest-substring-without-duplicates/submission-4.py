class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_count = 0
        seen = set()
        j = 0
        for i in range(len(s)):
            right = s[i]
            while right in seen:
                seen.remove(s[j])
                j += 1
            seen.add(right)
            max_count = max(max_count, i - j + 1)
        return max_count