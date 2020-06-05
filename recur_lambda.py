lambda_factorial = lambda i:1 if i==0 else i*lambda_factorial(i-1)

print(lambda_factorial(4))
