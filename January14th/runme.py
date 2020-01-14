import Lab3
import math
import matplotlib.pyplot as py

#simple_progression = Lab3.Progression(2001)
#for value in simple_progression:
#    print(value)

r = float(input("Enter an r value between -1 and 1"))
start = int(input("Enter a starting value"))
geometric_progression = Lab3.GeometricProgression(r, start)
sum = 0
calculated_sum = start / ( 1 - r )
print("expected sum of the sum of the series{}^{}n + {}^{}n+1....".format(r, start, r, start) )

for value in geometric_progression:
    sum += value
    print(sum)
    if math.fabs(sum - calculated_sum) < .00001:
        break


fib_first_500 = []
fib = Lab3.FibonacciProgression()
numbers = 0
for value in fib:
    numbers += 1
    fib_first_500.append(value)
    if numbers == 500:
        break

print(fib_first_500)

occurrence = {
    "1": 0,
    "2": 0,
    "3": 0,
    "4": 0,
    "5": 0,
    "6": 0,
    "7": 0,
    "8": 0,
    "9": 0
}

for fib_value in fib_first_500:
    if fib_value != 0:
        stringy_fib = str(fib_value)
        occurrence[stringy_fib[0]] += 1

x_axis = [str(key) for key in occurrence.keys()]

py.plot(list(occurrence.keys()), list(occurrence.values()))
py.show()