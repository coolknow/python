# #修改字符串大小写
# name = "jason hu"
# print(name.title())
# print(name.upper())
# print(name.lower())

# #合并，拼接字符串
# hello = "Hello"
# print(hello + ", " + name.title() + "!")

# #添加制表符(\t)换行符(\n)来添加空白
# print("\tPython")
# print("\nPython")
# print("people: \n\tJason\n\tLeo")

#删除空白
#末尾
sent1 = "I like fishes! "
print(sent1.rstrip())
#开头
sent2 = " I like fishes!"
print(sent2.lstrip())
#两头
sent3 = " I like fishes! "
print(sent3.strip())

