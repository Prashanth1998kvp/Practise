l = "automation"
print(l[::-1])
e = []
for i in l:
    e = [i] + e
print(e)

if e == l:
    print("pal")
else:
    print("not a pal")


a = "madam"
p = a[::-1]
print(p)
if a == p:
    print("pal")
else:
    print("not a pal")



x = [2,1,4,7,4,9,1]

smallest = float('inf')
second_smallest = float('inf')
for i in x:
    if i < smallest:
        second_smallest = smallest
        smallest = i

    elif i < second_smallest and i != smallest:
        second_smallest = i
print(second_smallest)
