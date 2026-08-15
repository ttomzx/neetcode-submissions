class Solution:
    def isValid(self, s: str) -> bool:
        myStack = []

        for ch in s:
            if ch == '(' or ch == '{' or ch == '[':
                myStack.append(ch)

            else:
                if not myStack: return False

                if ((ch == ')' and myStack[-1] == '(') or
                    (ch == '}' and myStack[-1] == '{') or
                    (ch == ']' and myStack[-1] == '[')):
                    
                    myStack.pop()
                else: return False

        if not myStack: return True
        else: return False