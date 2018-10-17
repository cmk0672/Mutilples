# If we list all the natural numbers below 10 that are multiples of 3 and 5
# we get 3,5,6 and 9. The sum of these multiples is 23.
# Find the sum of all the multiples of 3 or 5 below 1000.

# Korean (1000 미만의 3과 5의 배수의 합을 구하시오)
number_list = []
for number in range(1000):
    if number % 3 == 0 or number % 5 == 0:
        number_list.append(number)
        total_3and5 = sum(number_list)
print(total_3and5)


