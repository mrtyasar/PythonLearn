class Point:
    def move(self):
        print('Move!')
    def draw(self):
        print('Draw!')

point1 = Point()
point1.draw()
point1.move()
point1.x = 10
print(point1.x)
point1.y = 20
print(point1.y)

point2 = Point()
point2.x = 1
print(point2.x)


# egzersiz

class Person:
    def __init__(self,name):
        self.name = name
    def talk(self):
        print(f'Hi, I am {self.name}')

john = Person('John Smith')
print(john.name)
john.talk()

bob = Person('Bob Smith')
bob.talk()