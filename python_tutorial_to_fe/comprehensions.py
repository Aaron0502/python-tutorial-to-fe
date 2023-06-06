names = ['Bob', 'Tom', 'alice', 'Jerry', 'Wendy', 'Smith']
new_names = [name.upper() for name in names if len(name) > 3]
print(new_names)  # ['ALICE', 'JERRY', 'WENDY', 'SMITH']

nums = [num for num in range(30) if not (num % 3)]
print(nums)  # [0, 3, 6, 9, 12, 15, 18, 21, 24, 27]

list_demo = ['Google', 'Facebook', 'Taobao']
new_dict = {key: len(key) for key in list_demo}
print(new_dict)  # {'Google': 6, 'Facebook': 8, 'Taobao': 6}

my_dict = {num ** 2: num ** 3 for num in (2, 4, 6)}
print(my_dict)  # {4: 8, 16: 64, 36: 216}

my_set = {num ** 2 for num in (1, 2, 3)}
print(my_set)  # {1, 4, 9}

a = {x for x in 'abracadabra' if x not in 'abc'}
print(a)  # {'r', 'd'}

a = (x for x in range(1, 10))  # 返回的是生成器对象
a = tuple(a)  # 使用 tuple() 函数，可以直接将生成器对象转换成元组
print(a)  # (1, 2, 3, 4, 5, 6, 7, 8, 9)
