def multiply(a = 0, b = 0):
    accumulator = 0
    for i in range(b):
      accumulator = accumulator + a
    return accumulator

def exponent(a = 0, b = 0):
    accumulator = 0
    for i in range(b):
      accumulator = accumulator + a
    return accumulator

def square(num):
  return multiply(num, num)
  

result = multiply(arg1 = 5, arg2 = 7)
print(result)

result = multiply()
print(result)

result = exponent(a = 2, b = 3)
print(result)

result = square(2)
print(result)