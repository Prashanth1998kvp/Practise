from numpy.ma.core import count

arr = [("Apple", 100), ("Banana", 40), ("Orange", 60)]
my_dict = dict(arr)
print(my_dict)
# print(my_dict["Banana"])
# my_dict.update({"Grapes": 70})
# print(my_dict)
# my_dict.update({"Apple": 120})
# print(my_dict)
# my_dict.pop("Orange")
# print(my_dict)

my_dict.update({"Kiwi" : 80})

for key in my_dict.items():
    print(key)

for key , value in my_dict.items():
    print(key,"->", value)

count = 0
for key in my_dict.values():
    if count > 50:
        count += 1
print(count)