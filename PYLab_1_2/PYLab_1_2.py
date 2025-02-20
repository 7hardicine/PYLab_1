import math

print('Input m:')
m = float(input())

t = 2.8
y = 3.6 * (math.sin(m) - math.cos(m) ** 2)/t
print('The value of y = ', y)

if (y < 1):
    b = math.fabs(t + y)
else:
    b = math.fabs(t - y)

f = b**2 / (b + math.sin(y)**2)
print('The value of f = ', f)