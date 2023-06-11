list1 = ['Google', 1997, 2000]
list2 = [1, 2, 3, 4, 5]
list3 = ["a", "b", "c", "d"]
list4 = ['red', 'green', 'blue', 'yellow', 'white', 'black']

my_list = [1, 2, 3, 4, 5]

print(my_list[0])  # 1
print(my_list[-1])  # 5
print(my_list[1:3])  # [2, 3]
print(my_list[:])  # [1, 2, 3, 4, 5]
print(my_list[::2])  # [1, 3, 5]

my_list = [1, 2, 3, 4, 5]
my_list[0] = 0       # 将第一个元素修改为0
my_list[1:3] = [6, 7, 8]  # 将第二个和第三个元素修改为6、7、8
print(my_list)  # [0 6, 7, 8, 4, 5]


list = ['Google', 1996, 1997, 2000]
print("原始列表 : ", list)  # 原始列表 :  ['Google', 1996, 1997, 2000]
del list[2]
print("删除第三个元素 : ", list)  # ['Google', 1996, 2000]
print("数组长度：", len(list))  # 数组长度： 3

print(len([1, 2, 3]))  # 3
print([1, 2, 3] + [4, 5, 6])  # [1, 2, 3, 4, 5, 6]
print(['Hi'] * 4)  # ['Hi', 'Hi', 'Hi’, 'Hi']
print(3 in [1, 2, 3])  # True

# 1 2 3
for x in [1, 2, 3]:
    print(x, end=" ")

print()

# 1 2 3 4 5
my_list = [1, 2, 3, 4, 5]
for i in range(len(my_list)):
    print(my_list[i], end=" ")

print()

# 1 2 3
my_list = [1, 2, 3]
i = 0
while i < len(my_list):
    print(my_list[i], end=" ")
    i += 1
print()

# 0 1 1 2 2 3
my_list = [1, 2, 3]
for index, element in enumerate(my_list):
    print(index, element, end=" ")

print()

my_list = [1, 2, 3]
a, b, c = my_list
print(a, b, c)  # 输出：1 2 3

my_list = [1, 2, 3]
a, *rest = my_list
print(a)    # 输出：1
print(rest)  # 输出：[2, 3]

my_list = [1, 2]
a, b, c = my_list if len(my_list) == 3 else [10, 20, 30]
print(a, b, c)  # 输出: 10 20 30

my_list = [1, 2, 3, 4]
# 交换第一个和第二个元素的位置
my_list[0], my_list[1] = my_list[1], my_list[0]
print(my_list)  # 输出：[2, 1, 3, 4]

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
a, b, c, *rest, y, z = my_list
print(rest)  # [4, 5, 6, 7, 8]

my_list = [1, [2, 3], 4]
a, (b, c), d = my_list
print(a, b, c, d)  # 输出：1 2 3 4
