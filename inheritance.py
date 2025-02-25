class Animal:
    def __init__(self, name,type ,sound):
        self.name=name
        self.type=type
        self.sound=sound

    def speak(self):
        print(f"{self.name} makes a {self.sound}")

    def __str__(self):
        return f"{self.name}, {self.type},{self.sound}"

class Dog(Animal):
    def __init__(self,name,type,sound,breed):
        super().__init__(name,type,sound)

    def speak(self):
        return f"A {self.name} barks!"


dog1=Dog("Rex","Domestic","bark","Pit bull")
print(dog1)
print(dog1.speak())
