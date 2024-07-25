max=5
thenum=9
while max>0:
    num=int(input("Guess the number 1 to 10: "))
    if num is not thenum:
        max-=1
    else:
        print("Great! you guessed it right.")
        break