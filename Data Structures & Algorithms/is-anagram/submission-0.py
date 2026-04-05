class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        tracker={}

        for char in s:
            if char in tracker:
                tracker[char]+=1
            else:
                tracker[char]=1
        
        for el in t:
            if el in tracker and tracker[el]!=0:
                tracker[el]-=1
            else:
                return False

        return all(count == 0 for count in tracker.values())