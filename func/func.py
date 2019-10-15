# # 打印一个简单的问候语  
# def great_user() :   # 定义一个函数
#     print("Hello!")  # 函数体 内的唯一一行代码

# great_user()


# # 向函数传递信息
# def great_user(username) :  # 这个函数要求你调用它时 给username指定一个值
#     print("Hello, " + username)  

# great_user("jason") # 调用这个函数时，可将一个名字传递给它
# # 👆这行代码的意思是：调用函数great_user()，并向它提供执行print语句所需的信息


# 实参和形参
"""
在上面的 great_user(username) 函数中，username 是形参
在调用函数时，great_user("jason")时，jason时实参
实参jason传递给函数great_user()，这个值被储存在形参username中
"""


# # 传递实参
# # 1.位置实参
# # 调用函数时，实参与形参要一一对应，最简单的办法是位置/顺序一致
# def describe_pet(type, name) :
#     print("My " + type + " is called " + name + ".")

# describe_pet("hamster", "harry")
# describe_pet("dog", "willie") # 函数和多次调用，且这种情况下，每次调用都需要传参


# # 2.关键字实参 —— 传递 “名称-值” 对
# # 无需考虑函数调用时 实参的顺序
# def describe_pet(type, name) :
#     print("My " + type + " is called " + name + ".")

# describe_pet(type="hamster", name="harry") # 将"hamster"储存在type中，将"harry"储存在name中


# # 3.默认值
# # 给每个形参指定 默认值
# # 如果提供了实参，就用实参；如果没提供实参，就用默认值
# def describe_pet(type, name="harry") :
#     print("My " + type + " is called " + name + "." + he)

# describe_pet(type="hamster")  # 前提是，传参时要有关键字，或者按照位置顺序传递


# 返回值
# return语句 将值返回到调用函数的代码行
# # 例：接收 “名” “姓”，返回完整姓名
# def name(fname, lname) :
#     fullName = fname + "." + lname
#     return fullName

# fullName = name("Jason", "Hu")
# print(fullName)


# # 让实参变成可选的
# def name(fname="", mname="", lname="") :
#     if mname : 
#         fullName = fname + "." + mname + "." + lname
#     else :
#         fullName = fname + "." + lname
#     return fullName

# fullName1 = name(fname="Jason", lname="Hu")
# fullname2 = name(fname="Harry", mname="J", lname="Poter")

# print(fullName1)
# print(fullname2)


# # 返回字典
# def build_person(fname, lname) :
#     person = {
#         "firstName" : fname,
#         "lastName" : lname
#     }
#     return person

# person = build_person("Jason", "Hu")
# print(person)

# def build_person(fname, lname, age="") :
#     person = {
#         "firstName" : fname,
#         "lastName" : lname
#     }
#     if age :
#         person["age"] = age
#     return person

# person = build_person("Jason", "Hu", 19)
# print(person)


# # 函数 与 while循环 结合
# def name(fname, lname) :
#     name = fname + "." + lname
#     return name

# while True :
#     print("\ntell me your name.('q' for quit)")
#     fname = input("fname: ")
#     lname = input("lname: ")
#     if fname == "q" :
#         break
#     elif lname == "q" :
#         break
#     else :
#         name = name(fname, lname)
#         print("hello, " + name)
















