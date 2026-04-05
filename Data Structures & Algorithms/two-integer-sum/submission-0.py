class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tracker={}
        # Check hashmap for complement, if doesnt exist, then add curr element to hashmap
        for i in range(len(nums)):
            complement=target-nums[i]
            if complement in tracker:
                return [tracker[complement], i]
            else:
                tracker[nums[i]]=i
        return []

        
        
        