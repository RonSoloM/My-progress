fruit = {"orange": "a sweet, orange, citrus fruit",
         "apple": "good for making cider",
         "lemon": "a sour, yellow citrus fruit",
         "grape": "a small, sweet fruit growing in bunches",
         "lime": "a sour, green citrus fruit"}

# while True:
#     dict_key = input("Please enter a fruit: ")
#     if dict_key == "quit":
#         break
#     if dict_key in fruit:
#         description = fruit.get(dict_key)
#         print(description)
#     else:
#         print("we don't have a " + dict_key)
#

shop_list = {"jeans": "Dark and blue jeans",
             "t-shirt": "White and orange",
             "shoes" : "White nike shox",
             "jacket": "Leather coat",
             "hoddie": "Gangster hoddie as fk"
             }

while True:
    dict_key = input("Please Pick shop item : ")
    if dict_key == "quit":
        break
    if dict_key in shop_list:
        description = shop_list.get(dict_key)
        print(description)
    else:
        print("We don't have a " + dict_key)