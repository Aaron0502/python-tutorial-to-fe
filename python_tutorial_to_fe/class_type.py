class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say_hello(self):
        print(f'Hello, my name is {self.name}, I am {self.age} years old.')


person1 = Person('Alice', 18)
person2 = Person('Bob', 20)

person1.say_hello()  # 输出Hello, my name is Alice, I am 18 years old.
person2.say_hello()  # 输出Hello, my name is Bob, I am 20 years old.


class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1


p1 = Person("Tom")
p2 = Person("Jerry")
print(Person.count)  # 输出：2
print(p1.count)  # 输出：2


class Person:
    def __init__(self, name):
        self.name = name


p = Person("Tom")
print(p.name)  # 输出：Tom
p.name = "Jerry"
print(p.name)  # 输出：Jerry


class MyClass:
    attr = 0

    def __init__(self):
        self.attr = 1
        MyClass.attr += 1


instance = MyClass()

print(instance.attr)  # 1


class MyClass:
    count = 0

    def __init__(self):
        MyClass.count += 1

    @classmethod
    def get_count(cls):
        return cls.count


a = MyClass()
b = MyClass()
print(MyClass.get_count())  # 输出：2


class MyClass:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"Hello, my name is {self.name}.")


a = MyClass("Tom")
a.say_hello()  # 输出：Hello, my name is Tom.


class MyClass:
    @staticmethod
    def say_hello():
        print("Hello, world!")


MyClass.say_hello()  # 输出：Hello, world!


class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def say_hello(self):
        print(f'Hello, my name is {self.__name}, I am {self.__age} years old.')


p = Person('aaron', 27)
p.say_hello()  # Hello, my name is aaron, I am 27 years old.


class Animal:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"{self.name} says hello!")


class Flyable:
    def fly(self):
        print(f"{self.name} is flying!")


class Bird(Animal, Flyable):
    def chirp(self):
        print(f"{self.name} is chirping!")


b = Bird("Sparrow")
b.say_hello()  # 输出：Sparrow says hello!
b.chirp()  # 输出：Sparrow is chirping!
b.fly()  # 输出：Sparrow is flying!


class A:
    def say_hello(self):
        print("Hello from A")


class B:
    def say_hello(self):
        print("Hello from B")


class C(A, B):
    pass


class D(B, A):
    pass


c = C()
c.say_hello()  # 输出：Hello from A
d = D()
d.say_hello()  # 输出：Hello from B


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * other, self.y * other)

    def __truediv__(self, other):
        return Vector(self.x / other, self.y / other)

    def __str__(self):
        return f"({self.x}, {self.y})"


v1 = Vector(1, 2)
v2 = Vector(3, 4)

print(v1 + v2)  # 输出：(4, 6)
print(v1 - v2)  # 输出：(-2, -2)
print(v1 * 2)   # 输出：(2, 4)
print(v2 / 2)   # 输出：(1.5, 2.0)
