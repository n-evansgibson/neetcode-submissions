class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
  
        # Creates a hash set
        seen = set()
        
        # Iterate through list
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)
        
        return False
                

        