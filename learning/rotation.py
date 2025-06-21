
array=[1,2,3,4,5]
rotation=2
rotation=rotation%len(array)
reveres= [0]*len(array)

class rotate:
    def __init__(self,number_rotation: int,length:int):
        self.number_rotation=number_rotation
        self.reveres=[0]*length

    def right(self,array: list[int]) -> list[int]:
        for ind in range(self.number_rotation):
            self.reveres[ind] = array[len(array) - self.number_rotation+ind]

        for ind in range(len(array)-self.number_rotation):
            self.reveres[self.number_rotation + ind] = array[ind]
        return self.reveres

    def left(self,array: list[int]) -> list[int]:
        for ind in range(self.number_rotation):
            self.reveres[len(array) - self.number_rotation + ind] = array[ind]

        for ind in range(len(array) - self.number_rotation):
            self.reveres[ind] = array[self.number_rotation + ind]
        return self.reveres

obj=rotate(rotation,len(array))
print(obj.right(array))
print(obj.left(array))
