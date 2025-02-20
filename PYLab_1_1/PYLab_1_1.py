import math as m

eps_1 = 1.01
eps_0 = 0.885
R = 2.87

print('Input the distance between the disks:')
L = float(input())

if (L/R < 1):
    C = eps_1 * eps_0 * R * (m.pi * R / L + m.log(16 * m.pi * R / L) - 1)
    print('C = ', C);
else:
    print('I dont know the formula for L/R >= 1 :)')
        