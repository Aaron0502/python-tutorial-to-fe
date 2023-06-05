# 海象运算符
text = input("请输入一个字符串：")
if (n := len(text)) > 3:
    print(f"输入的字符串长度为{n}，超过了3个字符")
else:
    print(f"输入的字符串长度为{n}，不超过3个字符")

# in运算符

lst = [1, 2, 3]
print(2 in lst)  # 输出 True，因为列表 lst 包含值为 2 的元素
print(4 in lst)  # 输出 False，因为列表 lst 不包含值为 4 的元素

string = 'hello'
print('h' in string)  # 输出 True，因为字符串 string 包含字符 'h'
print('world' in string)  # 输出 False，因为字符串 string 不包含子串 'world'

# 身份运算符

a = [1, 2, 3]
b = a
print(b is a)  # 输出：True
print(b == a)  # 输出：True
b = [1, 2, 3]
print(b is a)  # 输出：false
print(b == a)  # 输出：True
