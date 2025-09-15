# TC: O(n*m) n = length of input list, m = maximum value in the input list (or values generated during merges)
# SC: O(n)
class Solution:
    def compute_gcd(self,num1,num2):
        ''' Step 1: Divide the larger number by the smaller number and note the remainder. 
            Step 2: Replace the larger number with the smaller number and the smaller number with the remainder. 
            Step 3: Repeat the process until the remainder is 0
            Step 4: The last non-zero remainder is the GCD. 
        '''        
        while num2 != 0:
            # reminder = num1 % num2
            # num1 = num2
            # num2 = reminder
            num1, num2 = num2, num1 % num2
        return num1
    # Slow approach
    # def compute_lcm(self, num1,num2):        
    #     greater = num1 if num1 > num2 else num2
    #     while True:
    #         if (greater % num1 == 0) and (greater % num2 == 0):
    #             lcm=greater
    #             break
    #         greater += 1
    #     return  lcm
    def compute_lcm(self, num1, num2, gcd):
        ''' Step 1: Multiply the two numbers (num1 and num2)
            Step 2: Divide the product by their GCD (greatest common divisor)
        '''
        return abs(num1 * num2) // gcd

    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack = []
        for num in nums:
            stack.append(num)
            while len(stack) >= 2:
                num1 = stack[-1]
                num2 = stack[-2]
                gcd = self.compute_gcd(num1, num2)
                if gcd > 1:
                    lcm = self.compute_lcm(num1, num2,gcd)
                    stack.pop()
                    stack.pop()
                    stack.append(lcm)
                else:
                    break
        return stack