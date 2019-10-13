# # 创建并打印一个字典
# alien_0 = {"color": "green", "points": 5}
# # 空字典
# alien_0 = {}

# print(alien_0["color"])
# print(alien_0["points"])

# 在Python中，字典是一系列“键-值”对
# 上面👆的代码展示了如何访问字典中的值

# # 如何添加“键-值”对
# alien_0["x_position"] = 0
# alien_0["y_position"] = 25
# print(alien_0)

# # 如何修改“键-值”对
# alien_0["x_position"] = 200
# print(alien_0)

# alien_0 = {"color": "green", "points": 5}

# alien_0["x_position"] = 0 # 添加“键-值”对
# alien_0["y_position"] = 25
# alien_0["speed"] = "slow"

# if alien_0["speed"] == "slow" :
#     alien_0["x_position"] += 1
# elif alien_0["speed"] == "medium" :
#     alien_0["x_position"] += 2
# else :
#     alien_0["x_position"] += 3

# print(alien_0["x_position"])

# # 删除“键-值”对
# # 使用del语句时，必须指定 “字典名” 和 “键名”
# del alien_0["points"]
# print(alien_0)

# # 遍历字典
# # 遍历所有“键-值”对
# words = {
#     "sector" : "a particular area of business in economy",
#     "dominant" : "strong or most used",
#     "diminish" : "get weaker"
# }

# for word, meaning in words.items() : # 将每个键付给临时变量word，将每个值付给临时变量meaning，列表名后要加 .items()
#     print(word + ": \n\t" + meaning)

# # 遍历所有键
# for word in words.keys() : # 只将每个键赋给临时变量word，使用 .keys()
#     print(word)

# # 遍历所有值
# # 方法一
# for word in words.keys() :
#     print(words[word])

# # 方法二
# for meaning in words.values() :
#     print(meaning)

# # 判断 键 是否存在于字典中
# new_word = "apple"

# if new_word not in words.keys() :
#     print("this new word is not in word list.")

# # 按顺序遍历字典中的所有键
# for word in sorted(words.keys()) : # sorted()函数的运用
#     print(word)

# # 无重复的提取所有值
# for meaning in set(words.values()) :
#     print(meaning)

# # 嵌套
# # 在字典中嵌套列表
# alien_0 = {
#     "color" : "green",
#     "points" : "5"
# }

# alien_1 = {
#     "color" : "yellow",
#     "points" : "10"
# }

# alien_2 = {
#     "color" : "red",
#     "points" : "15"
# }

# aliens = [alien_0, alien_1, alien_2]

# for alien in aliens :
#     print(alien)

# # 用代码自动生成👽
# aliens = []

# for alien_num in range(30) :
#     new_alien = {"color":"green", "points":"5"}
#     aliens.append(new_alien)

# for alien in aliens[0:3] : # 修改前3个
#     if alien["color"] == "green" :
#         alien["color"] = "yellow"
#         alien["points"] = "10"

# for alien in aliens[:5] :
#     print(alien)

# print("...")

# 在字典中添加列表
pizza = {
    "crust" : "thick",
    "toppings" : ["mushrooms", "extra cheese"]
}

for topping in pizza["toppings"] :
    print(topping)
    