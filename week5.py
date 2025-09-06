#Activity 1: creating a parent class with its child
class Car:
    def __init__(self, model, price):
        self.model = model
        self.price = price
    def output(self):
        return f"The car {self.model} has a price of {self.price}"



class Manufacture(Car):
    def __init__(self,model, price, manufacture):
        super().__init__(model, price)
        self.manufacture = manufacture
    def output(self):
        super().output()
        return f"It was manufactured in {self.manufacture}"

m = Manufacture("g20", 34534.90, "Germany")
print(m.output())

#Activity 2: using polymorphism

class Car:
     name = 'Mercedes'
     def move(self):
         return f'A {self.name} is driving on the street'
class Plane:
     name = 'private jet'
     def move(self):
         return f'A {self.name} is flying on the runway'
     
for vehicle in [Car(), Plane()]:
    print(vehicle.move())





