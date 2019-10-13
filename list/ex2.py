#你的切片，我的切片
nums = [x for x in range(1,21)]

print("the first three itenms in the list are: ")

for num in nums[:3] :
    print(num)

print("three items from the middle of the list are: ")

for num in nums[8:11] :
    print(num)

print("the last three items in the list are: ")

for num in nums[-3:] :
    print(num)

#你的pizza，我的pizza
my_pizzas = ["a", "b", "c", "d"]
friend_pizzas = my_pizzas[:]

my_pizzas.append("e")
friend_pizzas.append("f")

print("my favorite pizzas are: ")
for pizza in my_pizzas :
    print(pizza)

print("my friend's favorite pizzas are: ")
for pizza in friend_pizzas :
    print(pizza)