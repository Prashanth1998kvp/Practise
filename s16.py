# a = int(input("enter the number"))
# if a % 2 == 0:
#     print("even")
# else:
#     print("odd")

# s = "kvp"
# a = ""
# for i in s:
#     a = i + a
#     print(a)
# print(s[::-1])
#
# p = s.strip()
# print(p)

n = int(input("Enter a number: "))
if n <= 1:
    print("it is not a prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("not a prime")
            break
    else:
        print("prime")



n = int(input("Enter a number: "))
if n <=1:
    print("it is not a prime")
else:
    for i in range(2, n):
        if n % i == 0:
            print("not a prime")
            break
        else:
            print("prime")
    else:
        print("prime")
# n = int(input("Enter a no "))
# if n > 1:
#     for i in range(2,n):
#         if n % i == 0:
#             print("not prime")
#         else:
#             print("prime")


# a = 10
# b = 30
#
# a, b = b, a
# print("a:",a,"b :",b)