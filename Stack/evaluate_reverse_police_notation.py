"""You are given an array of strings tokens that represents an arithmetic expression in a
Reverse Polish Notation.

Evaluate the expression. Return an integer that represents the value of the expression.

Note that:

The valid operators are '+', '-', '*', and '/'.
Each operand may be an integer or another expression.
The division between two integers always truncates toward zero.
There will not be any division by zero.
The input represents a valid arithmetic expression in a reverse polish notation.
The answer and all the intermediate calculations can be represented in a 32-bit integer.
 """
from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        while len(tokens) > 1:
            for i, token in enumerate(tokens):
                if token in '+/*-':
                    op = tokens.pop(i)
                    n1 = int(tokens.pop(i-1))
                    n2 = int(tokens.pop(i-2))
                    if token == '+':
                        tokens.insert(i-2, str(n1+n2))
                    elif token == '*':
                        tokens.insert(i - 2, str(n1 * n2))
                    elif token == '/':
                        tokens.insert(i - 2, str(int(n2/n1)))
                    elif token == '-':
                        tokens.insert(i - 2, str(n2 - n1))
                    break
        return int(tokens[0])

