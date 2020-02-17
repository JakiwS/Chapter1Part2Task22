t = input()
sign = t[-1]
t = int(t[0:-1])
if sign == 'C' or sign == 'c':
    t = (t * (9/5) + 32)
    print(str(t) + 'F')
elif sign == 'F' or sign == 'f':
    t = ((t - 32) * (5/9))
    print(str(t) + 'C')