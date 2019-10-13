# # 人

# users = {  
#     "leo" : {              
#         "fname" : "Linshuo",
#         "lname" : "Zhang",
#         "age" : 19,
#     },   

#     "jason" : {
#         "fname" : "Haodong",
#         "lname" : "Hu",
#         "age" : 19,
#     },

#     "jack" : {
#         "fname" : "Wenda",
#         "lname" : "Lu",
#         "age" : 20,
#     }
# }

# for user, user_info in users.items() :
#     print("user name: " + str(user))
#     print("\tfname: " + str(user_info["fname"]))
#     print("\tlname: " + str(user_info["lname"]))
#     print("\tage: " + str(user_info["age"]))

leo = {              #创建个人信息
    "fname" : "Linshuo",
    "lname" : "Zhang",
    "age" : 19,
}  

jason = {
    "fname" : "Haodong",
    "lname" : "Hu",
    "age" : 19,
}

jack = {
    "fname" : "Wenda",
    "lname" : "Lu",
    "age" : 20,
}

users = {                # 创建集体信息
    "leo" : leo,
    "jason" : jason,
    "jack" : jack
}

for user, user_info in users.items() :
    print("user name: " + str(user))
    print("\tfname: " + str(user_info["fname"]))
    print("\tlname: " + str(user_info["lname"]))
    print("\tage: " + str(user_info["age"]))