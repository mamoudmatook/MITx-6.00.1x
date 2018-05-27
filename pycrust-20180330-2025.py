PyCrust 0.9.8 - The Flakiest Python Shell
Python 2.7.14+ (default, Feb  6 2018, 19:12:18) 
[GCC 7.3.0] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> iteration = 0
... count = 0
... while iteration < 5:
...     # the variable 'letter' in the loop stands for every 
...     # character, including spaces and commas!
...     for letter in "hello, world": 
...         count += 1
...     print("Iteration " + str(iteration) + "; count is: " + str(count))
...     iteration += 1