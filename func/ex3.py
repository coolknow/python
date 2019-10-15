# # 城市名
# def city_country(city, country) :
#     cc = city + "," + country
#     return cc

# name = city_country("santiago", "chile")
# print(name)


# # 专辑
# def make_album(singer, name, num="") :
#     album = {
#         "singer" : singer,
#         "album_name" : name,
#     }
#     if num :
#         album["num"] = num
#     return album

# album1 = make_album("jack", "high", 10)
# album2 = make_album("lili", "love")

# print(album1)
# print(album2)


# # 用户的专辑
# def make_album(singer, name, num="") :
#     album = {
#         "singer" : singer,
#         "album_name" : name,
#     }
#     if num :
#         album["num"] = num
#     return album

# while True :
#     print("\nenter singer, name of album, and num here ('q' for quit): ")
#     singer = input("singer: ")
#     if singer == "q" :
#         break    
#     name = input("name: ")
#     if name == "q" :
#         break    
#     num = input("num(optional): ")
#     if num == "q" :
#         break
#     album = make_album(singer, name, num)
#     print(album)


