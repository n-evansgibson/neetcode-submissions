class Solution:
    def isValid(self, s: str) -> bool:

        # If the length of the string is odd, return false
        if (len(s) % 2 == 1): 
            return False

        # If first character is backward, return False
        if (not self.isForward(s[0])): return False

        # Create a stack to store the first half of the array
        stack = []
        
        # Traverse the string
        for c in s:
            # If character is forward facing, add to stack
            if self.isForward(c):
                stack.append(c)
            # If character is backward facing, check if on top of stack
            else:
                if (len(stack) == 0): return False
                matching_character = stack.pop()
                if (self.oppChar(matching_character) != c):
                    return False
        
        return (len(stack) == 0)

            

    

    def oppChar(self, c: str) -> str:
        if (c == '{'): 
            return '}'
        elif (c == '['):
            return ']'
        else: 
            return ')'

    def isForward(self, c: str) -> bool:
        forwards = ['[', '{', '(']
        return (c in forwards)



        




        