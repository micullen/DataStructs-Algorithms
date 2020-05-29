"""
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

Example 1:
Input: "()"
Output: true

Example 2:
Input: "()[]{}"
Output: true

Example 3:
Input: "(]"
Output: false

Example 4:
Input: "([)]"
Output: false

To approach this problem we will use a stack. Add all opening parantheses to the stack, then if a closing paranthesis
matches a bracket on the top of the stack, remove it as they match.
"""


from structs import Stack

class Solution:
    @staticmethod
    def is_valid(string: str) -> bool:
        """
        Premise for this operation is that if the opening bracket matches the closing bracket next to it, remove from the stack
        If the stack isn't empty after iterating through the whole process, it's invalid.
        :type string: str
        :rtype: bool
        """
        stack = Stack()
        opens = ['{', '[', '(']
        closes = ['}', ']', ')']
        matches = {'[': ']', '{': '}', '(': ')'}

        if len(string) == 0:
            return False

        for bracket in string:
            if bracket in opens:
                stack.push(bracket)

            if bracket in closes:
                x = stack.top()
                y = matches[stack.top()]
                if bracket == matches[stack.top()]:
                    stack.pop()
                else:
                    # i.e. ( ] is invalid always
                    return False

        if stack.length() == 0:
            return True
        else:
            return False


print(Solution.is_valid('[]'))
print(Solution.is_valid('[)'))
print(Solution.is_valid('{[]}'))
print(Solution.is_valid('([{}])'))
print(Solution.is_valid('()[]{}'))
