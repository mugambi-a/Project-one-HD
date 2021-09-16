Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> class Flight():
    def_init_(self, capacity):
    self.capacity=capacity
    self.passengers=[]
def add_passengers(self,name):
    if not self.open_seats():
        return False
    self.passengers.append(name)
    return True
def open_seats(self):
    return self.capacity-len(self.passengers)
fliht=Flight(3)
people=['joe','mike','adam','peter','cate','joy']
for person on people:
    if flight.add_passenger(person):
        print(f' Added {person}to flight successfully')
        else:
            print(f' No available seats for {person}')

SyntaxError: invalid syntax
>>> name='joe'
>>> print(name[0])
j
>>> print(name[1])
o
>>> name=['joe','mike','joy','felix']
>>> print(name)
['joe', 'mike', 'joy', 'felix']
>>> print[0]
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    print[0]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> print(name[0])
joe
>>> 
KeyboardInterrupt
>>> print(name[1])
mike
>>> neme.append('Gito)
	    
SyntaxError: EOL while scanning string literal
>>> name.append('Gito)
	    
SyntaxError: EOL while scanning string literal
>>> name.append('Gito')
>>> print(name)
['joe', 'mike', 'joy', 'felix', 'Gito']
>>> s=set()
>>> s.add(1)
>>> s.add(2)
>>> s.add(3)
>>> s.add(1)
>>> s.add(3)
>>> print(s)
{1, 2, 3}
>>> s.remove(0)
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    s.remove(0)
KeyError: 0
>>> s.remove(1)
>>> print(s)
{2, 3}
>>> houses={'harry', 'gryffindor','draco'}
>>> print(houses[0])
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    print(houses[0])
TypeError: 'set' object is not subscriptable
>>> print(houses['harry'])
Traceback (most recent call last):
  File "<pyshell#25>", line 1, in <module>
    print(houses['harry'])
TypeError: 'set' object is not subscriptable
>>> houses={'harry': 'gryffindor','draco':'slytherin'}
>>> print(houses['harry'])
gryffindor
>>> houses['Hermi']='gryffidor'
>>> print(house['Hermi'])
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    print(house['Hermi'])
NameError: name 'house' is not defined
>>> print(houses['Hermi'])
gryffidor
>>> s=set()
>>> s.add(3)
>>> s.add(5)
>>> s.add(7)
>>> s.add(5)
>>> print(s)
{3, 5, 7}
>>> s.add(2)
>>> print(s)
{2, 3, 5, 7}
>>> print(f'the set has {len(s)} elements')
the set has 4 elements
>>> print('the set has {len(s)} elements)
      
SyntaxError: EOL while scanning string literal
>>> print('the set has {len(s)} elements')
the set has {len(s)} elements
>>> for i in [0,1,2,3,4,5]
	print(i)
	
SyntaxError: invalid syntax
>>> for i in [0,1,2,3,4,5]
SyntaxError: invalid syntax
>>> for i in[0,1,2,3,4,5]
SyntaxError: invalid syntax
>>> for i in [0,1,2,3,4,5]:
print(i)
SyntaxError: expected an indented block
>>> print(s)
{2, 3, 5, 7}
>>> print(i)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    print(i)
NameError: name 'i' is not defined
>>> for i in [0,1,2,3,4,5]:
	print

	
<built-in function print>
<built-in function print>
<built-in function print>
<built-in function print>
<built-in function print>
<built-in function print>
>>> i=[0,1,2,3,4,5]
>>> for i in [0,1,2,3,4,5]:
	print(i)

	
0
1
2
3
4
5
>>> 