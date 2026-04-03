"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = "2"
Output: ["a","b","c"]
"""

class Solution:
    def letterCombinations(self, digits):
        if not digits:
            return []
        
        res = []
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        
        def backtracking(index, path):
            if index == len(path):
                res.append(path)
                return
            for char in mapping[digits[index]]:
                backtracking(index + 1, path + char)
                
        backtracking(0, '')
        return res

# Test cases
solution = Solution()
print(solution.letterCombinations("23"))
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(solution.letterCombinations("2"))
# Output: ["a","b","c"]
# Each digit has 3 or 4 choices (except for 7 and 9 which have 4 choices), so the total combinations can be calculated as the product of the number of choices for each digit.
# Time complexity: O(3^n * 4^m) where n is the number of digits that map to 3 letters (2, 3, 4, 5, 6, 8) and m is the number of digits that map to 4 letters (7 and 9). This is because each digit can lead to multiple combinations.
# Space complexity: O(n) for the recursion stack and O(3^n * 4^m) for the output list that contains all combinations.   