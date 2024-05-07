from typing import override

class Shape:
    def __init__(self,name:str,sides:int) -> None:
        self.name = name
        self.sides = sides
        
    def describe(self) -> None:
        print(f'{self.name} has {self.sides} sides')
        
    def shape_method(self) -> None:
        print(f'{self.name}: shape method')
        

class Square(Shape):
    def __init__(self,size:float) -> None:
        super().__init__('Square',4)
        self.size = size
    
    @override
    def describe(self) -> None:
        print(f'I am a square with size {self.size}')
        
class Polygon(Shape):
    def __init__(self, name: str, sides: int) -> None:
        super().__init__(name, sides)
        
    @override
    def describe(self) -> None:
       print(f'{self.name} is a ploygon with {self.sides} sides')
        

def main() -> None:
    sq: Square = Square(23)
    sq.describe()
    sq.shape_method()
    
    pent: Polygon = Polygon('Pentagon',5)
    pent.describe()
    
if __name__ == '__main__':
    main()