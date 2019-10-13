# 创建并打印嘉宾名单
name = ["Jason", "Leo", "Albert", "Jack", "Peter"]
for x in name :
    print("Hi, " + x + ". Welcome to this dinner!")

#有一名嘉宾不能来，修改嘉宾名单
notCome = "Jack"  
print(notCome + " cannot come.")

newName = "Levy"

i = 0
for x in name :
    if x == notCome :
        name[i]= newName
    i += 1

for x in name :
    print("Hi, " + x + ". Welcome to this dinner!")

#添加嘉宾
print("Wow, there is a bigger table! So, i need three more people in.")

name.insert(0, "Allen")
name.insert(3, "Mike")
name.append("Anderson")

for x in name :
    print("Hi, " + x + ". Welcome to this dinner!")

print("I'm sorry. Now, I can only invite two people to the dinner.")

#缩减名单
count  = len(name) + 1

for x in range (1, count - 2) :
    delName = name.pop()
    print("sorry, " + delName)

print(name)

for x in name :
    print( x + ", you are still in.")

print(len(name))
for x in range(len(name)):
    name.pop(x-1)

print(name)