class Animal:
    def __init__(self,name):
        self.name=name
    def speak(self):
        pass
    def print_me(self):
        print(f"{self.name}")

class Dog(Animal):
    def speak(self):
        pass
        # print(f"{self.name} wau wau")
class Meow(Dog):
    def speak(self):
        print(f"{self.name} is barking")
# dog=D
# dog.speak()
# dog.print_me()
# stusy=Meow("heihei")
# stusy.speak()
stutsy=Meow("heihei")
stutsy.speak()
stutsy.print_me()