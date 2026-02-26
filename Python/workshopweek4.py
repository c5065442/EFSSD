PS C:\Users\c5065442\OneDrive - Sheffield Hallam University\EFSSD\Python> python
Python 3.12.4 (tags/v3.12.4:8e8a4ba, Jun  6 2024, 19:30:16) [MSC v.1940 64 bit (AMD64)] on win32 
Type "help", "copyright", "credits" or "license" for more information.
>>> 1 + 1
2
>>> 5 - 3
2
>>> 10 / 3
3.3333333333333335
>>> 10*2
20
>>> 2**2        
4
>>> 3**2
9
>>> 2**3
8
>>> 5 + 6 * 2
17
>>>  (5 + 6) * 2
  File "<stdin>", line 1
    (5 + 6) * 2
IndentationError: unexpected indent
>>>  5 + 6 ** 3
  File "<stdin>", line 1
    5 + 6 ** 3
IndentationError: unexpected indent
>>> 5 + 6 **3
221
>>> (5 + 6) * 2
22
>>> 16 ** 0.5
4.0 
>>> item1 = "Ham"  
>>> item1
'Ham'
>>> print(item1)
Ham 
>>> 1 ==1
True
>>> 1 == 5
False
>>> 1 !=1
False
>>> 1 != 5
True
>>> 1 > 1
False
>>> 1 > 5
False
>>> 2 >=
  File "<stdin>", line 1
    2 >=
        ^
SyntaxError: invalid syntax
>>> 2>= 2
True
>>> 6 >= 10
False
>>> 12 < 5
False
>>> 12
12
>>> 12 < 5
False
>>> 12 <= 9
False
>>> 4 < 12
True
>>>
>>> 12 <= 22
True
>>> print("Welcome to SHU")
Welcome to SHU
>>> Print("will this work?")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'Print' is not defined. Did you mean: 'print'?
>>> print("will this work?")
will this work?
>>> print("programming is fun!")
programming is fun!
>>> num1 = 22
>>> print("The value of num1 is ", num1)
The value of num1 is  22
>>> num2 = 44
>>> print(num1, num2)
22 44
>>> print(num1+num2)
66
>>> num1 = str(num1)
>>> print(num1, num2)
22 44
>>> print(num1+num2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> print(num1+num2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> print(num1+num2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: can only concatenate str (not "int") to str
>>> print(num1, num2)
22 44
>>> item1 = "eggs"
>>> item1
'eggs'
>>> print(item1)
eggs
>>> print("I like", item1)
I like eggs
>>> item2 = sandwich
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'sandwich' is not defined
>>> item2 ="sandwich"
>>> item2
'sandwich'
>>> item1 + item2 
'eggssandwich'
>>> print(item1 + item2)
eggssandwich
>>> print(item1, item2)
eggs sandwich
>>> print(item, " ", item2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'item' is not defined. Did you mean: 'item1'?
>>> print("I remove the plus sign and made use of the space and comma sign for the single space between item1 and item2")
I remove the plus sign and made use of the space and comma sign for the single space between item1 and item2
>>> print(item1, " ",item2)
eggs   sandwich
>>> print("I like", item1+ item2)
I like eggssandwich
>>> print("I like", item1, item2")
  File "<stdin>", line 1
    print("I like", item1, item2")
                                ^
SyntaxError: unterminated string literal (detected at line 1)
>>> print("I like", item1 item2".)
  File "<stdin>", line 1
    print("I like", item1 item2".)
                               ^
SyntaxError: unterminated string literal (detected at line 1)
>>> print("I like". item1 item2)
  File "<stdin>", line 1
    print("I like". item1 item2)
          ^^^^^^^^^^^^^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print("I like", item1, item2)
I like eggs sandwich
>>> print("I remove the plus sign and replace it with the comma sign in between the item1 and item2")
I remove the plus sign and replace it with the comma sign in between the item1 and item2
>>> num1 = 16
>>> print('num1 is', num1, 'and num2 is ', num2, '. The sum =' ,num1+num2)
num1 is 16 and num2 is  44 . The sum = 60
>>>  print(num1 + num2)
  File "<stdin>", line 1
    print(num1 + num2)
IndentationError: unexpected indent
>>> print("num1, num2)  
  File "<stdin>", line 1
    print("num1, num2)
          ^
SyntaxError: unterminated string literal (detected at line 1)
>>> print(num1 num2)
  File "<stdin>", line 1
    print(num1 num2)
          ^^^^^^^^^
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> print(num1, num2)
16 44
>>> print(item1 + item2)  
eggssandwich
print(num1, item1)
print(num1, num2)
>>> print(num1, item1)
16 eggs
>>> print(str(num1) + item1)
16eggs
>>>>>> print(str(num2) + item2)
44sandwich
>>> print("_".join("HELLO"))
H_E_L_L_O
>>> "***".join("12345")
'1***2***3***4***5'
>>> string1 = "HELLO SHEFFIELD"
>>> print("*".join(string1))
H*E*L*L*O* *S*H*E*F*F*I*E*L*D
>>> string2 = "HELLO SHEFFIELD UNITED ARE YOU PREPARED FOR THE WEEEKEND GAME FOR THEW WEEKEND"
>>> print("*".join(string2))
H*E*L*L*O* *S*H*E*F*F*I*E*L*D* *U*N*I*T*E*D* *A*R*E* *Y*O*U* *P*R*E*P*A*R*E*D* *F*O*R* *T*H*E* *W*E*E*E*K*E*N*D* *G*A*M*E* *F*O*R* *T*H*E*W* *W*E*E*K*E*N*D
>>> print("S*H*U" .split("*"))
['S', 'H', 'U']
>>> myChars = ("S*H*U" .split("*"))
>>> print(myChars)
['S', 'H', 'U']
>>> print(myChars[0])
 myDate = ("25/12/2021" .split("/"))
>>> myDay = myDate[0]
>>> myMonth = myDate[1]
>>> myYear =myDate[2]
>>> print("Christmas is on the " + myDay + "th day of the month")
Christmas is on the 25th day of the month