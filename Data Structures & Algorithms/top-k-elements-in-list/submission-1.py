class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        b=[]
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        db=sorted(d.items(), key=lambda item:item[1],reverse=True)
        for i in range(k):
            b.append(db[i][0])
        return b