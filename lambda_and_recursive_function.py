# Write a lambda function to find the biggest among 3 numbers
biggest = lambda a, b, c: max(a, b, c)

num = input("Enter the numbers (comma separated): ")
num = [int(num) for num in num.split(",")]

num1 = num[0]
num2 = num[1]
num3 = num[2]

print(biggest(num1, num2, num3))

# Write a recursive function to find Fibonacci series of given range

def fibonacci_series(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        # series = [0, 1]
        # for i in range(2, n):
        #     series.append(series[i - 1] + series[i - 2])
        # return series
        seq = fibonacci_series(n - 1)
        seq.append(seq[-1] + seq[-2])
        return seq

n = int(input("Enter the range: "))
print(fibonacci_series(n))