l = [1, 2, 2, 3, 4, 4]

seen = []
orgin = []

for i in l:
    if i in seen:
        seen.append(i)
    else:
        orgin.append(i)

print("duplicates:", seen)
print("unique:", orgin)




