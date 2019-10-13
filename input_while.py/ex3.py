# # 熟食店
# orders = ["a", "b", "c", "d"]
# finishs = []

# while orders :
#     creat = orders.pop()
#     print(creat + " is being cooked.")
#     finishs.append(creat)

# print(orders)
# print(finishs)

# 五香烟熏牛肉卖完了
orders = ["a", "b", "c", "d", "c", "c"]
finishs = []
print(orders)

print("no c")
while "c" in orders :
    orders.remove("c")

print(orders)

while orders :
    creat = orders.pop()
    print(creat + " is being cooked.")
    finishs.append(creat)

print(orders)
print(finishs)
