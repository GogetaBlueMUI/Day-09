max=20
number=[]
while True:
    num=input("Enter a number and type 'done' to exit: ")
    if num=='done':
        break
    num=float(num)
    if num>max:
        number.append(num)
print("Numbers greater than max cap: ", number)