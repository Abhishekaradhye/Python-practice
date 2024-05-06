# Given an array of integers nums and an integer target, without choosing same element again,
# return indices of the two numbers such that they add up to target.


class adding_couple:
    def twoSum(self, nums, target):
         for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j]== target:
                    return [i,j]
                
ab = adding_couple()
print(ab.twoSum([2,3,5,6], 9))