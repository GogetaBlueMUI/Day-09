total=0
digits=0
while True:
    num=input("Enter a number and type 'done' to exit: ")
    if num=='done':
        break
    num=float(num)
    total+=num
    digits+=1
print("Sum of numbers is: ", total)
print("Average of numbers is: ", total/digits)
