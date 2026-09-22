class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) == 1:
            return int(tokens[0])
    
        stack = []
        ops = {
            "+" : lambda a,b : a + b,
            "-" : lambda a,b : a - b,
            "*" : lambda a,b : a * b,
            "/" : lambda a,b : int(a/b)
        }
        
        for token in tokens:
            if token in ops:
                b = stack.pop()
                a = stack.pop()
                res = ops[token](int(a),int(b))
                stack.append(res)
            else:
                stack.append(token)

        return int(stack.pop())