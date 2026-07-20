class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       freq = {}

       for n in nums:
            freq[n] = freq.get(n, 0) + 1

       # Sort the dictionary keys based on their values (frequencies) in descending order
       sorted_elements = sorted(freq.keys(), key=lambda x: freq[x], reverse=True)

       return sorted_elements[:k]