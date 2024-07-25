number=[]
removed=[]
while True:
    num=input("Enter a number and type 'done' to exit: ")
    if num=='done':
        break
    num=float(num)
    number.append(num)
    for num in number:
        if num not in removed:
            removed.append(num)
print("New List: ", removed)