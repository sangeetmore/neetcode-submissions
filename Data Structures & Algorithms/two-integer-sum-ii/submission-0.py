class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        for _ in range(len(numbers)):
            total=numbers[i]+numbers[j]
            if total == target:
                return [i+1, j+1]
            elif total > target:
                j-=1
            elif total < target:
                i+=1
        return [i+1, j+1]