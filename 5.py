while True:
    str=input("Enter string: 'done' to exit and '#' at start to skip: ")
    if str=='done':
        break
    if str.startswith('#'):
       continue
    print("Line: ", str)