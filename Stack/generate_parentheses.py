"""Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses."""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def backtrack(open_n, close_n):
            if open_n == close_n == n:
                result.append("".join(stack))
                return

            if open_n < n:
                stack.append('(')
                backtrack(open_n+1, close_n)
                stack.pop()

            if close_n < open_n:
                stack.append(')')
                backtrack(open_n, close_n+1)
                stack.pop()

        backtrack(0,0)
        return result

if __name__ == '__main__':
    sol = Solution()
    result = sol.generateParenthesis(4)
    print()


