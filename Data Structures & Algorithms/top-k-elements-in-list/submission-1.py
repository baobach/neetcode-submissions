class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # input is an array and interger, expected output is a list of any numbers that
        # has the frequency equal or higher than the given interger.
        # 1. Create a set of nums array which serves as a key for the hash table of num:freq
        num_keys = set(nums)
        num_freq = dict.fromkeys(num_keys,0)
        for num in nums:
            num_freq[num] += 1
        # 2. Sorted the num_freq in the desc order by value
        num_freq_desc = dict(sorted(num_freq.items(), key = lambda items: items[1], reverse = True))
        # 3. Return top k answer
        answer = list(num_freq_desc.keys())[:k]
        return list(answer)

