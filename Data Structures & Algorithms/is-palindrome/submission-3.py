import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
 
        # Define pointers
        L = 0
        R = len(s) - 1

        while (L < R):

            # Go to the closest alphanumeric letter
            while (L < R) and not s[L].isalnum():
                L += 1
            while (R > L) and not s[R].isalnum():
                R -= 1
            # If the letters do not match, return false
            if s[L].lower() != s[R].lower():
                return False

            # Otherwise move pointers
            L += 1
            R -= 1 

        return True
        