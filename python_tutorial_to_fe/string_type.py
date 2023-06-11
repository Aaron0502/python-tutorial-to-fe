s = "hello"
print(s[0])  # 输出字符 'h'
print(s[1])  # 输出字符 'e'
print(s[2])  # 输出字符 'l'
print(s[3])  # 输出字符 'l'
print(s[4])  # 输出字符 'o'

s = "hello"
print(s[1:4])  # 输出子串 'ell'
print(s[:3])   # 输出子串 'hel'
print(s[2:])   # 输出子串 'llo'
print(s[::2])  # 输出隔一个字符取一个字符的子串 'hlo'

a = "Hello"
b = "Python"

print("a + b 输出结果：", a + b)  # a + b 输出结果： HelloPython
print("a * 2 输出结果：", a * 2)  # a * 2 输出结果： HelloHello
print("a[1] 输出结果：", a[1])  # a[1] 输出结果： e
print("a[1:4] 输出结果：", a[1:4])  # a[1:4] 输出结果： ell

# H 在变量 a 中

if ("H" in a):
    print("H 在变量 a 中")
else:
    print("H 不在变量 a 中")

# M 不在变量 a 中
if ("M" not in a):
    print("M 不在变量 a 中")
else:
    print("M 在变量 a 中")

print(r'\n')  # \n
print(R'\n')  # \n

x = 1
print(f'{x+1}')  # 2

name = "Alice"
age = 18
# 输出 "My name is Alice, and I'm 18 years old."
print(f"My name is {name}, and I'm {age} years old.")

a = 123
b = 456
# 输出 "The sum of 123 and 456 is 579."
print(f"The sum of {a} and {b} is {a + b}.")

a = 123
b = 456
print(f"{a + b = }")  # 输出 "a + b = 579"
