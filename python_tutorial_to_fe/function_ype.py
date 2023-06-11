def add(x, y=0):
    """
    计算两个数的和

    :param x: 第一个数
    :param y: 第二个数，默认为0
    :return: 两个数的和
    """
    return x + y


def greet(name, message):
    print(f"{message}, {name}!")


greet(name="Alice", message="Hello")  # 输出 "Hello, Alice!"
greet(message="Hi", name="Bob")  # 输出 "Hi, Bob!"


def greet(name, message, times):
    for i in range(times):
        print(f"{message}, {name}!")


greet("Alice", "Hello", times=3)    # 输出 "Hello, Alice!" 三次
greet("Bob", times=2, message="Hi")  # 输出 "Hi, Bob!" 两次


def my_func(message):
    my_sub_func(message)  # 调用my_sub_func()在其声明之前不影响程序执行


def my_sub_func(message):
    print('Got a message: {}'.format(message))


my_func('hello world')  # Got a message: hello world

a = 3


def modify_global_var():
    global a
    a += 1  # 注意：不能直接写 global a += 1


modify_global_var()
print(a)  # 4

a = 3


def test_inline_var():
    a = 4
    print(a)  # 4


test_inline_var()


def outer():
    x = "local"

    def inner():
        nonlocal x  # nonlocal关键字表示这里的x就是外部函数outer定义的变量x
        x = 'nonlocal'
        print("inner:", x)  # inner: nonlocal
    inner()
    print("outer:", x)  # outer: nonlocal


outer()


def counter():
    count = 0

    def inner():
        nonlocal count
        count += 1
        return count
    return inner


c = counter()
print(c())  # 输出1
print(c())  # 输出2
print(c())  # 输出3


def f(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)


f(10, 20, 30, d=40, e=50, f=60)


def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)


printinfo(70, 60, 50)


def printinfo(arg1, **vardict):
    "打印任何传入的参数"
    print(arg1)
    print(vardict)


# 调用printinfo 函数
printinfo(1, a=2, b=3)

# 输出
# 1
# {'a': 2, 'b': 3}


def my_function(a: int, b: str) -> float:
    return a + b


print(my_function(1, 2))  # 3
print(my_function('21', '32'))  # 2132
