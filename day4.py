#ValidParentheses-Leetcode#20
class Solution:
    def isValid(self, s: str) -> bool:
     
        matches = {
    ')': '(',
    ']': '[',
    '}': '{'
}
        stack = []
        for char in s:
            if char in matches:      # closing bracket
                top = stack.pop() if stack else '#'
                if top!=matches[char]:
                    return False
            else:                    # opening bracket
                stack.append(char)
        return len(stack)==0