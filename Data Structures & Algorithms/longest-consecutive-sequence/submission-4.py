class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==1: return 1
        tracker=set(nums)
        count=0
        for num in tracker:
            if num-1 not in tracker:
                current_num = num
                current_count = 1
                while current_num+1 in tracker:
                    current_num+=1
                    current_count+=1
                count = max(count, current_count)
        return count
            
            
        