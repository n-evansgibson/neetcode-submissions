class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        # Edge case
        if len(s) == 1: return 1

        # Find the most frequent character in s
        chars = defaultdict(int)
        for char in s: 
            chars[char] = chars.get(char, 0) + 1

        max_char = max(chars, key=chars.get)

        # Sliding window over the string
        chars = defaultdict(int)
        max_freq = 0
        res = 0
        l = 0

        for r in range(len(s)):
            chars[s[r]] += 1
            max_freq = max(max_freq, chars[s[r]])

            while (r - l + 1) - max_freq > k:
                chars[s[l]] -= 1
                l += 1

            res = max(res, r - l + 1)

        return res
                
            



            


        

        
        




        





        
        