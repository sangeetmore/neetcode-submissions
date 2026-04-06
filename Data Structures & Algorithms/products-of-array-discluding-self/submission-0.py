class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod=[1]*len(nums)
        for i in range(len(nums)):
            prod_l=1
            prod_r=1
            suff,pre=1,1
            
            for a in range(0,i):
                prod_l=pre*nums[a]
                pre=prod_l
            for b in range(len(nums)-1, i, -1):
                prod_r=suff*nums[b]
                suff=prod_r
            
            prod[i]= prod_l*prod_r
        return prod
        