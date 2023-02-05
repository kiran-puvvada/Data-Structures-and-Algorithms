class Solution:
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in  range(1,len(nums)):
                if i!=j:
                    if nums[i]+nums[j]==target:
                        return [i,j]
nums = [2,7,11,15]
target=9
obj=Solution()
print(obj.twoSum(nums,target))