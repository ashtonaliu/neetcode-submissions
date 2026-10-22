class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if len(trust) == 0:
            return 1
        t = {}
        seen = set()
        tj = -1
        for p in trust:
            if p[0] not in seen:
                seen.add(p[0])
                if len(seen) == n:
                    return -1
            if p[1] not in t:
                t[p[1]] = 0
            t[p[1]] += 1
            if t[p[1]] == (n - 1):
                if p[1] not in seen:
                    tj = p[1]
        return tj
        