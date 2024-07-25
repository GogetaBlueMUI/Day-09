num = int(input("Enter the number of terms: "))

# Initializing the first two Fibonacci numbers
a, b = 0, 1

print("Fibonacci Series:")
for _ in range(num):
    print(a, end=" ")
    a, b = b, a + b