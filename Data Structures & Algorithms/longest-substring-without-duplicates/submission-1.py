class Solution:
    def lengthOfLongestSubstring_slow(self, s: str) -> int:

        # Edge cases
        if (len(s) < 2):
            return len(s)

        # Sliding window with hash
        longest_substring = 0
        window = set()

        for L in range(len(s)):            
            R = L
            while (R < len(s)):
                next_s = s[R]
                
                # Case #1: next value can be part of sequence
                if next_s not in window:
                    window.add(next_s)
                    R += 1
                # Case #2: next value is a duplicate, found full substring
                else:
                    longest_substring = max(longest_substring, len(window))
                    window.clear()
                    break

        return longest_substring

    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l = 0
        res = 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res, r - l + 1)

        return res


