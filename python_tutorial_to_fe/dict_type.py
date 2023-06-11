my_dict = {'name': 'a', 'age': 3, 'name': 'b'}
print(my_dict)  # {'name': 'b', 'age': 3}

a = (1, 2)
my_dict = {"name": 'a', 'age': 3, a: 32}
print(my_dict)  # {'name': 'a', 'age': 3, (1, 2): 32}

my_dict = {"name": 'a', 'age': 3}
print(my_dict['name'])  # a

my_dict = {"name": 'a', 'age': 3}
my_dict['name'] = 'b'
my_dict['class'] = 3
print(my_dict['name'])  # b
print(my_dict['class'])  # 3

my_dict = {"name": 'a', 'age': 3}
del my_dict['name']
print(my_dict)  # {'age': 3}

my_dict = {'name': 'John', 'age': 30, 'city': 'New York'}
name, age, city = my_dict
print(name)  # 输出 'John'
print(age)   # 输出 30
print(city)  # 输出 'New York'
