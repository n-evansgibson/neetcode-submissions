class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # Add all of the elements to a hash map
        numsHash = {}
        for i, n in enumerate(nums):
            numsHash[n] = i

        # Method we know that for any two elements in the set,
        # a + b = t. I will iteratve through the list one more
        # time to check for some b s.t. b = t - a. 
        
        for i, n in enumerate(nums):
          
          # Find what value would be needed for nums[i] to work
          difference = target - n;

          if difference in numsHash and numsHash[difference] != i:
            return [i, numsHash[difference]]

        # If we cannot find a pair (this should not happen), return empty array
        return []

        


        