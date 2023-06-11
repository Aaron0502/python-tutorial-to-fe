# 变量赋值
counter = 100          # 整型变量
miles = 1000.0       # 浮点型变量
name = "runoob"     # 字符串

print(counter)
print(miles)
print(name)

a = b = c = 1
d, e, f = 1, 2, "runoob"
print(a, b, c, d, e, f)


# 空值

x = None
if x is None:
    print("x is None")
else:
    print("x is not None")

print(type(x))

# 函数和类


def square(x):
    return x ** 2


nums = [1, 2, 3, 4, 5]
squares = map(square, nums)
print(list(squares))  # 输出：[1, 4, 9, 16, 25]


def add(x):
    def inner(y):
        return x + y
    return inner


add_five = add(5)
print(add_five(3))  # 输出：8


class MyClass:
    pass


my_object = MyClass()
print(type(my_object))  # 输出： <class '__main__.MyClass'>


# 类型判断

x = 123
if type(x) == int:
    print("x is an integer")
else:
    print("x is not an integer")

x = 123
if isinstance(x, int):
    print("x is an integer")
else:
    print("x is not an integer")

x = 123
if isinstance(x, (int, float, str)):
    print("x is an integer, float or string")
else:
    print("x is not an integer, float or string")


class A:
    pass


class B(A):
    pass


print(isinstance(A(), A))  # returns True
print(type(A()) == A)      # returns True
print(isinstance(B(), A))   # returns True
print(type(B()) == A)       # returns False


# 类型转换

num_int = 123
num_flo = 1.23

num_new = num_int + num_flo

print("datatype of num_int:", type(num_int))
print("datatype of num_flo:", type(num_flo))

print("Value of num_new:", num_new)
print("datatype of num_new:", type(num_new))

x = True + 2
print(x)  # 输出3，True被转换为1
y = False + 2.0
print(y)  # 输出2.0，False被转换为0.0
