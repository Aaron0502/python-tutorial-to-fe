age = int(input("请输入你家狗狗的年龄: "))
print("")
if age <= 0:
    print("你是在逗我吧!")
elif age == 1:
    print("相当于 14 岁的人。")
elif age == 2:
    print("相当于 22 岁的人。")
elif age > 2:
    human = 22 + (age - 2)*5
    print("对应人类年龄: ", human)

# 1 到 100 之和为: 5050
n = 100
sum = 0
counter = 1
while counter <= n:
    sum = sum + counter
    counter += 1

print("1 到 %d 之和为: %d" % (n, sum))


# 1 2 3
for x in [1, 2, 3]:
    print(x, end=" ")

print()


def do_nothing():
    pass
