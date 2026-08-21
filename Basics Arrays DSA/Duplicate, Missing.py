class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        count=0
        ct=[]
        for jl in nums:
            for el in nums:
                if jl>el:
                    count+=1
            ct.append(count)
            count=0
        return ct

# But we can have a optimal solution??

        