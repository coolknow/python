#每条if语句的的核心都是一个值为True或False的表达式，这种表达式被称为条件测试
#Python根据条件测试的值为True还是False来决定是否执行if语句中的代码
#如果条件测试的值为True，Python就执行紧跟在if后面的代码；如果为False，Python就忽略这些代码

#将变量值与当前值进行比较
#一个等号是陈述 “将变量设置为...”
#两个等号是发问 “变量的值是...吗？”

# #检查特定值是否在列表中
# name = ["jason", "leo", "mike", "stephen", "Alpha"]
# print("leo" in name)
# print("jack" in name)
# print("lili" not in name)

#布尔表达式（条件测试）

#if语句：测试+操作

#使用if语句处理列表
# requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']
# for requested_topping in requested_toppings:
#     if requested_topping == "green peppers" :
#         print("Sorry, we don't have green peppers.")
#     else :
#         print("Adding " + requested_topping + ".")
    
# print("\nFinished making your pizza!")

# requested_toppings = []

# if requested_toppings == [] :
#     print("do you want original taste?")
# else :
#     for requested_topping in requested_toppings :
#         print("Adding " + requested_topping + ".")

# #检查配料表
# available_toppings = ['mushrooms', 'olives', 'green peppers', 'pepperoni', 'pineapple', 'extra cheese']
# requested_toppings = ['mushrooms', 'green peppers', 'cola']

# for requested_topping in requested_toppings :
#     if requested_topping in available_toppings :
#         print("Adding " + requested_topping + ".")
#     else :
#         print("Sorry, we don't have " + requested_topping + " now.")

    
        

