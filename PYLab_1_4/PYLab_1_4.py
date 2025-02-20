import math as m

print('Input diameter N:')
N = float(input())

C =  m.pi * N 
Flag = C / 8

print('The lenth of flag = ', Flag)

S = N

print('Input the number of flag:')
Flag_num = int(input())

if (Flag_num <= 4):
    S += Flag_num * Flag
else:
    S += (Flag_num - 4) * Flag

print('Total distance = ', S)