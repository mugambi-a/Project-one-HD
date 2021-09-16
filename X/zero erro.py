
x=float(input('x:'))
y=float(input('y:'))  
try:
    result=x/y
    print(f'{x}/{y}={result}')
except ZeroDivisionError as e:
    e=result
    print(f'{e}Error:Cannot divide by 0.')



import os
os.system('pause')
