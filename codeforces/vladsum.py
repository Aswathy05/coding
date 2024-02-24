import sys
sys.stdin=open("input.txt","r")
sys.stdout=open("output.txt","w")
def digit_sum(num):
    # Function to calculate the sum of digits for a number
    total = 0
    while num > 0:
        total += num % 10
        num //= 10
    return total

def sum_of_digit_sums(n):
    # Function to calculate the sum of digit sums for numbers from 1 to n

    # Calculate the sum for complete cycles of 1 to 9
    sum_1_to_9 = 45 * (n // 9)

    # Calculate the sum for complete cycles of 10 to 99
    sum_10_to_99 = 450 * (n // 90)

    # Calculate the sum for complete cycles of 100 to 999
    sum_100_to_999 = 4500 * (n // 900)

    # Calculate the sum for numbers from 1000 to n
    sum_from_1000_to_n = 0
    for i in range(1000, n + 1):
        sum_from_1000_to_n += digit_sum(i)

    # Calculate the sum for remaining numbers from 1 to 6
    sum_remaining = sum(range(1, min(n % 9 + 1, 7)))

    # Total sum is the sum of all calculated sums
    total_sum = sum_1_to_9 + sum_10_to_99 + sum_100_to_999 + sum_from_1000_to_n + sum_remaining

    return total_sum

# Input the value of n
for i in range(int(input())):   

    n = int(input())
# Calculate and print the sum of digit sums for numbers from 1 to n
print(sum_of_digit_sums(n))
