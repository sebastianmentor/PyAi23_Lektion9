class Person:
    def __init__(self, name) -> None:
        self._name = name

    def get_name(self):
        return self._name
    
class Bil:
    def __init__(self, brand:str, year:int) -> None:
        self._brand = brand
        self._year = year
        self.__driver = None

    def get_info(self):
        return f'{self._brand=}, {self._year=}, {self.__driver.get_name() if self.__driver else ""}' 
    
    def _has_driver(self)->bool:
        return False if self.__driver == None else True
    
    def put_driver_in_drivingseat(self,driver:Person):
        if self._has_driver():
            print('Already has a driver')
        else:
            self.__driver = driver

    def remove_driver(self,driver:Person):
        if driver is self.__driver:
            self.__driver = None
        else:
            print('You are not the driver of this car!!')

    def who_is_driver(self):
        if not self._has_driver():
            print('No')
        else:
            print(self.__driver.get_name())

person = Person('Sebastian')
person2 = Person('Kalle')
my_car = Bil('bmw', 1995)

print(my_car.get_info())
my_car.put_driver_in_drivingseat(person)
my_car.who_is_driver()

my_car.remove_driver(person2)
print(my_car.get_info())
my_car.remove_driver(person)
print(my_car.get_info())



