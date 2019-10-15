# # 三明治
# def describe(*toppings):
#     print("Customer want: ", toppings)

# describe("mushroom", "vegetables", "beef")


# # 用户简介
# def build_profile(fname, lname, **user_info) : # 形参 **user_info 中的两个星号让Python创建一个名为user_info的 空字典，并将收集到的所有 名称-值 对都封装到这个字典中。
#     """创建一个字典，其中包含我们知道的有关用户的一切"""
#     profile = {}
#     profile["first_name"] = fname
#     profile["last_name"] = lname
#     for key, value in user_info.items() : # 在这个函数中，可以像访问其他字典那样访问user_info中的 名称-值 对。
#         profile[key] = value
#     return profile

# user_info = build_profile("Jason", "Hu", nationality="China", sex="male", age=19)
# print(user_info)


# # 汽车
# def make_car(maker, num, **infos) :
#     car = {}
#     car["maker"] = maker
#     car["num"] = num
#     for key, value in infos.items() :
#         car[key] = value
#     return car

# car = make_car('subaru', 'outback', color='blue', tow_package=True)
# print(car)








