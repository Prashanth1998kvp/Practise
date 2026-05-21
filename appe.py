# arr = (1, 2, 3, 4, 5, 4)
#
# if len(arr) == len(set(arr)):
#     print("True")
# else:
#     print("False")

arr = (1, 2, 3, 4, 5, 4)

s = []
flag = True

for i in arr:
    if i in s:
        flag = False
        break
    else:
        s.append(i)
print(s)
print(flag)


