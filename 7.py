N = int(input("Enter the value of N: "))
sum_squares = 0
for i in range(1, N + 1):
    sum_squares += i * i
print("The sum of the squares of the first", N, "natural numbers is:", sum_squares)
