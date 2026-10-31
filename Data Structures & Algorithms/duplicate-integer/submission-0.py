class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Convert the list into a dict. Since dict only contains unique keys, len of dict keys always <= len of the list. If len(dict.keys) == len(list) they they don't have duplicates
        return len(set(nums)) < len(nums)