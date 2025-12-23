# Given an integer array nums, return true if any value 
# appears more than once in the array, otherwise return false.

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        x=set()
        for i in nums:
            if i in x:
                return True
            else:
                x.add(i)
        return False

# Example usage:
# sol = Solution()
# print(sol.hasDuplicate([1, 2, 3, 1]))  # Output: True
# print(sol.hasDuplicate([1, 2, 3, 4]))  # Output: False

# other solutions:
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False

class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False
    
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) < len(nums)