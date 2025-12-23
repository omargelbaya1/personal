# Given an array of integers nums and an integer target, return the indices i and j such 
# that nums[i] + nums[j] == target and i != j.

# You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

# Return the answer with the smaller index first.

#my solution is:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                    if nums[i] + nums[j] == target:
                        return [i,j]
        return []
    
# Example usage:
solution = Solution()
print(solution.twoSum([2,7,11,15], 9))  # Output: [0, 1]
print(solution.twoSum([3,2,4], 6))      # Output: [1, 2]
print(solution.twoSum([3,3], 6))      # Output: [0, 1]

#more Examples:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # val -> index

        for i, n in enumerate(nums):
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i