class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        result,powerX=set(),1
        while powerX < bound:
            powerY=1
            while powerX+powerY <= bound:  
                result.add(powerX+powerY)
                if y==1: break
                powerY*=y
            if x==1: break
            powerX*=x

        return list(result)
