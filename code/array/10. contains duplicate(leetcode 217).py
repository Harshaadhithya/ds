class Solution:
    def containsDuplicate(self, nums):
        if len(set(nums))==len(nums):
            return False
        else:
            return True
        """we can also use this below code, but in leetcode it says time limit exceeded"""
        # for num in nums:
        #     if num in temp_list:
        #         return True
        #     else:
        #         temp_list.append(num)
        # return False

s=Solution()
print(s.containsDuplicate([1,2,3,4,5,6,7,2,9]))