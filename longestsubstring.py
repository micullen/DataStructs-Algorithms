"""
Given a string, find the length of the longest substring without repeating characters.

Example 1:

Input: "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
"""

# Use sliding window method

class Solution:
    @staticmethod
    def lengthOfLongestSubstring(string):
        """
        :type string: str
        :rtype: int
        """
        chars = []
        for char in string:
            chars.append(char)

        sub_strings = []
        j = 0
        for i in range(1, len(chars), 1):
            sub_string = chars[j: i]
            val = chars[i]
            if chars[i] in sub_string:
                sub_strings.append(sub_string)


                while chars[i] in sub_string:
                    j += 1
                    sub_string = chars[j: i]


        sub_strings.append(sub_string)

        max_str = ''
        max_len = 0
        for strings in sub_strings:
            if len(strings) > max_len:
                max_str = strings
                max_len = len(strings)

        return max_str, max_len


string, length = Solution.lengthOfLongestSubstring('aaa')
print(f'largest string is {string} with length {length}')

string, length = Solution.lengthOfLongestSubstring('abcdea')
print(f'largest string is {string} with length {length}')

string, length = Solution.lengthOfLongestSubstring('abcabcaedfg')
print(f'largest string is {string} with length {length}')

string, length = Solution.lengthOfLongestSubstring('abcabcaedfgfeeeeeeeeeeeeeabcdefghijklm')
print(f'largest string is {string} with length {length}')

