class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        lookup = {}
        
        for index, num in enumerate(nums):
            verify = target-num
            if num in lookup:
                return [lookup[num],index]
            lookup[verify] = index
        return []