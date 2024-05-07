class Car:
    
    #class attribute
    SPEED_LIMIT_KM: float = 104
    
    def __init__(self,brand:str,wheels:int) -> None:
        #instance attribute
        self.brand = brand
        self.wheels = wheels
        
    def turn_on(self) -> None:
        print(f'Turning on : {self.brand}')
    
    def turn_off(self) -> None:
        print(f'Turning off: {self.brand}')

    def drive(self,km:float) -> None:
        print(f'Driving: {self.brand} for {km} km')
    
    def describe(self) -> None:
        print(f'{self.brand} is a car with {self.wheels} wheels')
    
def main() -> None:
    BMW: Car = Car('BMW',4)
    BMW.describe()
    BMW.turn_on()
    BMW.drive(10)
    BMW.turn_off()
    
    Volvo: Car = Car('Volvo',10)
    Volvo.describe()
    Volvo.turn_on()
    Volvo.drive(10)
    Volvo.turn_off()
    

    
if __name__ == '__main__':
    main()    