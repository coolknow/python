# # 从1数到5
# num = 1
# while num <= 5 :
#     print(num)
#     num += 1


# # 用户决定何时退出
# prompt = "\nTell me something, and I will repeat it back to you:"  
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':      
#     message = input(prompt)      
#     if message != "quit" :
#         print(message) 


# # 使用标志
# prompt = "\nTell me something, and I will repeat it back to you:"  
# prompt += "\nEnter 'quit' to end the program. "
# message = ""

# active = True

# while active :
#     message = input(prompt)
#     if message == "quit" :
#         active = False
#     else :
#         print(message)


# # 使用break退出循环
# prompt = "\nTell me something, and I will repeat it back to you:"  
# prompt += "\nEnter 'quit' to end the program. "
# message = ""

# while True : # 无限循环
#     message = input(prompt)
#     if message == "quit" :
#         break
#     else :
#         print(message)


# # 使用continue
# # 我的算法
# num = 1

# while num <= 10 :
#     if  (num % 2) != 0 :
#         num += 1
#         continue
#     else :
#         print(num)
#         num += 1

# # 别人的算法
# x = 0
# while x <= 10 :
#     x += 1
#     if (x % 2) == 0 :
#         print(x)
#     else :
#         continue


# # 删除包含特定值的所有列表元素
# pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
# print(pets)
# while 'cat' in pets:    # 如果不用循环，remove("cat")只删除第一个cat
#     pets.remove('cat')
# print(pets)


# 填充字典
responses = {}

active = True

while active :
    name = input("give me a name: ")
    response = input("what is the response: ")
    responses[name] = response
    
    repeat = input("do you want to continue (y/n) : ")
    if repeat == "y" :
        print(" ")
        continue
    else :
        print("\nresult:")
        active = False

for name, response in responses.items() :
    print("\t" + name + ": " + response)

print("---end---")