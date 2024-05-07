from typing import Self

class Person:
    def __init__(self,name:str,age:int) -> None:
        self.name = name
        self.age = age
    
    def __str__(self) -> str:
        return f'{self.name}: {self.age} year old'
    
    def __eq__(self, other: Self) -> bool:
        return self.age == other.age
    
    
def main():
    Mari: Person = Person('Mari Dada',40)
    print(Mari)
    
    Soma: Person = Person('Soma Dada',26)
    print(id(Soma))
    Soma1: Person = Person('Soma Dada',26)
    print(id(Soma1))
    
    print(Soma == Soma1)
    

if __name__ == '__main__':
    main()
    