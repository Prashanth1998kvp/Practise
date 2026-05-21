# @param x: int
# @return: string

def checkOddEven(x):
    # code here

    if x % 5 == 0:
        print("even")

    elif x % 2 != 0:
        print("odd")

    else:
        print("no")
print(checkOddEven(4))
print(checkOddEven(5))

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("even")
else:
    print("odd")