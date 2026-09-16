class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # Create stack and list to store result
        stack = []
        length = len(temperatures)
        result = [0] * length

        # Traverse through the list. We are guaranteed at least 
        # two elements in the list to start
        for i, temp in enumerate(temperatures):

            # If there are currently lesser values on the stack, 
            # and the value currently on top of the stack is 
            # strictly greater than all of those elements, pop
            # and calculate difference.
            
            while stack and temp > stack[-1][0]:
                stack_t, stack_i = stack.pop()
                result[stack_i] = i - stack_i
            stack.append((temp, i))

        return result





        
        