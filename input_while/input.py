# 函数input() 的作用：让程序暂停，等待用户输入一些文本。获取用户输入后，Python将其储存在一个变量中，以方便使用。

# message = input("Tell me somthing, and I will repeat it back to you: ")
# print(message)

'''
函数input() 接受一个参数：即要向用户显示的提示或说明，让用户直到该如何做。
在上面这个事例中，Python运行第一行代码时，用户将看到提示Tell me somthing, and I will repeat it back to you: 
程序等待用户输入，并在用户按回车键后继续运行。
输入储存在变量message中，接下来的print(message)将把输入呈现给用户

input()函数 将输入作为字符串类型
如果要将输入作为整数类型，需要改变数据类型 int()
'''

# # 运算符
# print(4 % 3) # 输出余数

# # 判断奇偶
# x = input("num: ")
# x = int(x)
# if (x % 2) == 0 :
#     print(str(x) + " is even.")
# else :
#     print(str(x) + " is odd.")

# # input()提示语句为两行
# prompt = "If you tell us who you are, we can personalize the messages you see."
# prompt += "\nWhat is your first name? "

# name = input(prompt)
# print("\nHello, " + name + "!")