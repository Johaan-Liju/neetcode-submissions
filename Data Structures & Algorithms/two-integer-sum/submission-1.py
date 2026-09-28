class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff={}
        for i,j in enumerate(nums):
            di=target-j
            if di in diff:
                return [diff[di],i]
            diff[j]=i
