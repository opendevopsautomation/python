'''
rule:1 ()=1
rule:2 if AB => A+B
        A=()=1
        B=()=1
rule:3 (A)=2*A   means if a string closed by parentheses
        A=()
        (())=>(1)=> 2*1=>2
'''
class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        result=[]
        for i in S:
            if i == '(':
                result.append(i)
            else:
                innerscore=0
                while result[-1] != '(' and result: 
                    innerscore+=result.pop()

                result.pop()
                if  innerscore == 0:  
                    result.append(1)
                else:
                    result.append(2*innerscore)

        return sum(result)                        