class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        # Calculate the product of all numbers combined
        total_product = 1
        zero_count = 0
        for num in nums:
            if num:
                total_product *= num
            else:
                zero_count += 1
            if zero_count > 1: return [0] * len(nums)
            

        # Create the output array
        solution = [0] * len(nums)
        for i, num in enumerate(nums):
            if zero_count == 1:
                solution[i] = 0 if (num != 0) else total_product
            else:
                solution[i] = total_product // num

        return solution

        

        