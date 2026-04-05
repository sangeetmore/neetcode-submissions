import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapper={}
        
        for num in nums:
            if num in mapper:
                mapper[num]+=1
            else:
                mapper[num]=1
                
        heap=[]
        for item,freq in mapper.items():
            heapq.heappush(heap,(-freq, item))
        
        res=[]
        
        while k>0:
            val,key = heapq.heappop(heap)
            res.append(key)
            k-=1

        return res
    
        
        

            

        