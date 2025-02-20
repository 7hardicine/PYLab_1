import math as m

print('Input the value of t:')
t = float(input())

x = 6 * (2 * t + m.sin(2 * t))
y = 6 * (t - m.cos(2 * t))

print('The value of x = ', x, ', the value of y = ', y)

if (x > 0 and y > 0):
    print('The hand is to the right and higher')
elif (x > 0 and y < 0):
    print('The hand is to the right and lower')
elif (x < 0 and y > 0):
    print('The hand is to the left and higher')
else:
    print('The hand is to the left and lower')
