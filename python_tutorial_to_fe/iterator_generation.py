my_list = [1, 2, 3, 4, 5]
my_iterator = iter(my_list)
while True:
    try:
        item = next(my_iterator)
        print(item)
    except StopIteration:
        break

my_list = [1, 2, 3, 4, 5]
for item in my_list:
    print(item)


def my_generator(limit):
    i = 0
    while i < limit:
        yield i
        i += 2


my_gen = my_generator(10)
while True:
    try:
        item = next(my_gen)
        print(item)
    except StopIteration:
        break

my_gen = my_generator(10)
for item in my_gen:
    print(item)
