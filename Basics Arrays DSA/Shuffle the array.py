class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans=[]
        i=0
        while i<n:
            ans.append(nums[i])
            ans.append(nums[n+i])
            i+=1
        return ans

 # what if we would had to do this with for loops
#  for i in range(n):
#     ans.append(nums[i])
#     ans.append(nums[n+i])
# return ans
