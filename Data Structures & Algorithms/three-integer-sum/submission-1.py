class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        # Create a list to store the result
        solution = []
        nums_len = len(nums)

        # Sort the array
        nums.sort()

        for i in range(nums_len):
            
            # Edge cases
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Create target
            target = nums[i]
            
            # Implement two sum on remaining elements
            L, R = i + 1, nums_len - 1
            while (L < R):

                # If values match the target, add to solution
                result = target + nums[L] + nums[R]
                if (result == 0):
                    new_sol = [target, nums[L], nums[R]]
                    if new_sol not in solution:
                        solution.append([target, nums[L], nums[R]])
                    L += 1
                    R -= 1
                    
                # Adjust L and R based on result
                elif (result < 0):
                    L += 1
                else:
                    R -= 1

        return solution

                

                

