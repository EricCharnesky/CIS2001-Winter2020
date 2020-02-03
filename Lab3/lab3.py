import Progression


fib = Progression.FibonacciProgression()

count = 1

for n in fib:
    count += 1
    print(n)

    if count > 20:
        break
