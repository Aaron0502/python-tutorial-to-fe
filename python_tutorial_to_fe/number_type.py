from decimal import Decimal
import math
import random

print(True + True)  # 2
print(False + True)  # 1

a = 123              # 十进制
b = 0b1010           # 二进制
c = 0o777            # 八进制
d = 0x1a             # 十六进制

print(a, b, c, d)    # 输出：123 10 511 26

print(0.1 + 0.2)  # 0.30000000000000004

print(Decimal('0.1') + Decimal('0.2'))  # 输出：0.3

print(17 / 3)  # 5.666666666666667
print(17 // 3)  # 5
print(17 % 3)  # 2
print(15 / 3)  # 5.0

print(abs(-3))  # 3
print(divmod(5, 3))  # (1, 2)
print(max(21, 43, 12, 4))  # 43
print(min(21, 43, 12, 4))  # 4
print(pow(2, 32))  # 4
print(round(7.36, 1))  # 7.4
print(sum((21, 43, 12, 4)))  # 80
print(math.floor(7.36))  # 7
print(math.ceil(7.36))  # 8
print(math.pi)  # 3.141592653589793
print(math.e)  # 2.718281828459045

print(random.random())
print(random.randint(1, 10))
print(random.uniform(1, 10))
print(random.choice(['apple', 'banana', 'orange']))
seq = ['apple', 'banana', 'orange']
random.shuffle(seq)
print(seq)
print(random.sample(range(1, 10), 3))
print(random.gauss(0, 1))
