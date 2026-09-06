class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = {}

        for n in nums:
            hashmap[n] = hashmap.get(n, 0) + 1

        pairs = list(hashmap.items())

        pairs.sort(key=lambda x: x[1])

        result = []

        for i in range(k):
            result.append(pairs.pop()[0])

        return result