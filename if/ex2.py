# #以特殊方式和管理员打招呼
# #处理没有用户的情形
# user_names = ["Jason", "Leo", "Alpha", "Admin"]

# if user_names == [] :
#     print("We need to find some users!")
# else :
#     for user_name in user_names :
#         if user_name.lower() == "admin" :
#             print("Hello admin, would you like to see a status report?")
#         else :
#             print("Hello " + user_name + ", thank you for logging in again.")

# #检查用户名
# current_users = ["jason", "leo", "mike", "john", "jack"]

# new_users = ["jason", "leo", "august", "sam", "ann"]

# for new_user in new_users :
#     if new_user in current_users :
#         print("please enter another username.")
#     else :
#         print("this name is not being used.")

#序数
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for num in nums :
    if num == 1 :
        print("1st")
    elif num == 2 :
        print("2nd")
    elif num == 3 :
        print("3rd")
    else :
        print(str(num) + "th")




