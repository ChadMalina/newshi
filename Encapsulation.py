class Person():
    def __init__(self,name,age,salary):
        self.name=name
        self._age=age
        self.__salary=salary
    def display2_info(self):
        return f"{self.name},{self._age},{self.__salary}"
    def display_info(self):
        print(f"The name is {self.name} am {self._age} old and {self.__salary}")


Display3_info=Person("Chad",
                     "22",
                     "800000"
                     )
print(Display3_info.name)
print(Display3_info._age)
print(Display3_info.__salary)

