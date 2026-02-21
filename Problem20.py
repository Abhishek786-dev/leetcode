"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false
"""

class Solution:
    def isValid(self, s: str) -> bool:
        map = {'(':')','{':'}','[':']'}
        stack = []
        for chr in s:
            if chr in map.keys():
                stack.append(chr)
            else:
                if len(stack) > 0:
                    if chr != map[stack.pop()]:
                        return False
                else:
                    return False
        
        return not stack
    
obj = Solution()
res = obj.isValid('')
print(res)