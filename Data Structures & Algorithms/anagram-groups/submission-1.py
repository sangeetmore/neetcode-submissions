from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # optimum solution
        # array of size 26, for storing the count of variable
        mapper=defaultdict(list)
        for i,t in enumerate(strs):
            count=[0]*26
            for el in t:
                idx = ord(el)-ord('a')
                count[idx]+=1
            mapper[tuple(count)].append(t)
        
        return list(mapper.values())
        