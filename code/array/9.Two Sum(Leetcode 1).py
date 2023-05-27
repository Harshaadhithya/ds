class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[j]+nums[i]==target:
                    return [i,j]

s=Solution()
print(s.twoSum([-1,-2,-3,-4,-5],-8))
print(s.twoSum([3,2,4],6))