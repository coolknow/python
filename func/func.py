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


# # 传递列表
# def great_users(names) :
#     for name in names :
#         msg = "Hello, " + name.title() + "!"
#         print(msg)

# usernames = ["jason", "leo", "jack"]
# great_users(usernames)


# # 在函数中修改列表
# def move(current_ls, new_ls) :
#     while current_ls :
#         current_l = current_ls.pop()
#         print("making " + current_l)
#         new_ls.append(current_l)

# def show(new_ls) :
#     for new_l in new_ls :
#         print(new_l + " is finished.")

# current_ls = ["a", "b", "c"]
# new_ls = []

# move(current_ls[:], new_ls) # 如果不想清空原始列表，可以把 副本 传过去。使用[:]
# show(new_ls)


# # 传递任意数量的实参
# def make_pizza(*toppings) : # 形参名 *toppings 中的星号 让Python创建一个名为topping的空元组，并将收到的所有值都封装到这个元组中。
#     """打印顾客点的所有配料"""
#     print(toppings) # 此处也可以用 for循环 进行遍历

# make_pizza("pepperoni")
# make_pizza("mushroom", "green peppers", "extra cheese")


# # 结合使用 位置实参 和 任意数量实参
# def make_pizza(size, *toppings) : 
#     """打印顾客点的所有配料"""
#     print(size, toppings) # , 可以区分 int 和 str

# make_pizza(6, "pepperoni")
# make_pizza(12, "mushroom", "green peppers", "extra cheese")


# # 使用任意数量的关键字实参
# def build_profile(fname, lname, **user_info) : # 形参 **user_info 中的两个星号让Python创建一个名为user_info的 空字典，并将收集到的所有 名称-值 对都封装到这个字典中。
#     """创建一个字典，其中包含我们知道的有关用户的一切"""
#     profile = {}
#     profile["first_name"] = fname
#     profile["last_name"] = lname
#     for key, value in user_info.items() : # 在这个函数中，可以像访问其他字典那样访问user_info中的 名称-值 对。
#         profile[key] = value
#     return profile

# user_info = build_profile("Jason", "Hu", nationality="China", sex="male")
# print(user_info)


# # 将函数储存在模块中
# import pizza

# pizza.make_pizza(16, "pepperoni")
# pizza.make_pizza(12, "mushroom", "green peppers", "extra cheese")


# # 导入特定函数
# """
# 导入模块中的特定函数
# from module_name import function_name

# 通过用逗号分隔函数名，可根据需要从模块中导入任意数量的函数
# from module_name import function_0, function_1, function_2

# 对于前面 pizza 的例子，如果只想导入要使用的函数，代码如下👇
# from pizza import make_pizza

# make_pizza(...) # 注意 此时在调用函数时，不用加模块名
# """


# # 使用as给函数指定别名
# # 例👇
# from pizza import make_pizza as mp
# mp(16, "pepperoni")


# # 使用as给模块指定别名
# # 例👇
# import pizza as p 

# p.make_pizza(16, "pepperoni")


# # 导入模块中的所有函数
# from pizza import *

# make_pizza(16, "pepperoni")
# make_pizza(12, "mushroom", "green peppers", "extra cheese")

 