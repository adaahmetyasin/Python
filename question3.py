#print("please enter a six-digit integer: ")
num = input("please enter a six-digit integer: ")
num = int(num)
for x in range(6):
    print(int(num%10))
    num = (num - (num%10)) / 10
    