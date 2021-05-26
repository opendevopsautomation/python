import operator
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) < 2:
            return tokens[0]
        ops = {'+' : operator.add,
               '-' : operator.sub,
               '*' : operator.mul,
               '/' : operator.truediv,
            }
        list=[tokens[0]]
        for i in range(len(tokens)) :
            if tokens[i] in ops.keys():
                ans=int(ops[tokens[i]] (list[~1],  list[~0]))
                list.pop()
                list.pop()
                list.append(ans)
            else:
                list.append(int(tokens[i]))
        return ans
        