def largest(array):
    large=0
    for num in array :
        if num>large:
            large=num
    return large
def lowest(array):
    low=999
    for num in array :
        if num<low:
            low=num
    return low
number=[]
while True:
    num=input("Enter a number and type 'done' to exit: ")
    if num=='done':
        break
    num=float(num)
    number.append(num)
print("Largest number: ", largest(number))
print("Lowest number: ", lowest(number))