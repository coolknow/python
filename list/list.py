# #修改列表元素
# tools = ["bike", "car", "bus", "plane"]

# tools[0] = "on feet"
# print(tools[0])

# #在列表末尾添加元素
# tools.append("taxi")
# print(tools)

# #插入元素
# tools.insert(0, "Uber")
# print(tools)

# #删除元素
# del tools[0]
# print(tools)

# lastChoice = tools.pop() # pop(这里面可以加入index)
# print(lastChoice)
# print(tools)

# #根据值删除元素
# x = "bus"
# tools.remove(x)
# print(x)
# print(tools)

# #生成列表
# x = range(1,21)
# print(x)

# place = ["Beijing", "London", "New York", "Paris", "Roma"]
# print(place)

# #临时逆序输出
# print(sorted(place, reverse = True))
# print(place)

# #逆序输出
# place.reverse()
# print(place)

# #改回来
# place.reverse()
# print(place)

# #永久性按照字母顺序排列列表中的元素
# place.sort()
# print(place)

# #逆序输出
# place.sort(reverse=True) 
# print(place) 

# # 生成一系列数字
# for x in range(1, 5):
#     print(x)

# #创建数字列表
# numbers = list(range(1, 5))
# print(numbers)

# #指定步长
# even_numbers = range(2, 11, 2)
# print(even_numbers)

# #1-10的平方
# squares = []

# for value in range(1, 11):
#     square = value ** 2 #临时变量square : 作为一个“中转站” 把每一个值传入特定的list中
#     squares.append(square)

# print(squares)

# #找最大值
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(max(nums))

# #找最小值
# print(min(nums))

# #求和
# print(sum(nums))

# #列表解析
# squares = [value**2 for value in range(1,11)]
# print(squares)

# #打印1-20
# for x in range(1,21):
#     print(x)

# #一百万
# mylist = [x for x in range(1, 1000001)]
# for x in mylist :
#     print(x)

# print(min(mylist))
# print(max(mylist))
# print(sum(mylist))

# #1-20里的奇数
# odd = [x for x in range(1, 21, 2)]
# for x in odd :
#     print(x)

# #3的倍数
# nums = [x for x in range(3, 31, 3)]
# for x in nums :
#     print(x)

# #立方, 解析列表
# nums = [x for x in range(1, 11)]
# triples = []
# for x in nums :
#     triple = x ** 3
#     triples.append(triple)

# print(triples)

# #使用列表的一部分
# #切片
# players = ['charles', 'martina', 'michael', 'florence', 'eli']
# print(players[-2:])

# #遍历切片
# for player in players[:3]:
#     print(player)

#复制列表
my_foods = ["pizza", "falafel", "carrot", "cake"]
#错误做法
friends_foods = my_foods
#正确做法
friends_foods = my_foods[:]

my_foods.append("cannoli")
friends_foods.append("ice cream")

print(my_foods)
print(friends_foods)



