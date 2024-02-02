import json
import timeit

#factorial python funtion with integer n
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
# utilizing timeit module  to time the execution of 100 times of factorial(100)
total_time0 = timeit.timeit(stmt="factorial(100)", setup="from __main__ import factorial", number=10000)

#printing out the results from the timeit module
print("factorialorial (10000 runs) " + str(total_time0))

#factorial python funtion with integer n using a for loop
def factorial1(n):
    result = 1
    for i in range(n, 0, -1):
        result = result * i
    return result

# utilizing timeit module  to time the execution of 100 times of factorial(100)
total_time_1 = timeit.timeit(stmt="factorial1(100)", setup="from __main__ import factorial1", number=1000)

#printing out the results from the timeit module
print("for loop method (1000 runs) " + str(total_time_1))

#factorial python funtion with integer n using a list comprehension
def factorial2(n):
    return 1 if n == 0 else n * factorial2(n - 1)

# utilizing timeit module  to time the execution of 100 times of factorial(100)
total_time_2 = timeit.timeit(stmt="factorial2(100)", setup="from __main__ import factorial2", number=1000)

#printing out the results from the timeit module
print("list comprehension method (1000 runs) " + str(total_time_2))