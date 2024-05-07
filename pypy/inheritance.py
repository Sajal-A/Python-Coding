class Animal:
    def __init__(self,name:str) -> None:
        self.name = name
    
    def drink(self) -> None:
        print(f'{self.name} is drinking')
    
    def eat(self) -> None:
        print(f'{self.name} is eating')
    
class Dog(Animal):
    def __init__(self, name: str, age:int) -> None:
        super().__init__(name)
        self.age = age
        
    def sound(self) -> None:
        print(f'{self.name} is barking')
        
    def rountine(self) -> None:
        self.eat()
        self.sound()
        self.drink()
        
class Cat(Animal):
    def __init__(self, name: str,age:int) -> None:
        super().__init__(name)
        self.age = age
    def sound(self) -> None:
        print(f'{self.name} is meowing')
        
    def rountine(self) -> None:
        self.eat()
        self.sound()
        self.drink()
        
        
        
def main() -> None:
    cat: Cat = Cat('Linda',10)
    dog: Dog = Dog('Bholu',12) 
    
    cat.rountine()
    dog.rountine()   
    
if __name__  == '__main__':
    main()