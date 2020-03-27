fib = [0,1]
while len(fib) < 10:
   fib.append(fib[-1]+fib[-2])
print(fib)