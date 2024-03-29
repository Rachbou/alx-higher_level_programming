##0x03. Python - Data Structures: Lists, Tuples##
#Requirements#
*Python Scripts*
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- The first line of all your files should be exactly #!/usr/bin/python3
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should use the pycodestyle (version 2.8.*)
- All your files must be executable
- The length of your files will be tested using wc
*C*
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
- All your files should end with a new line
- Your code should use the Betty style. It will be checked using betty-style.pl and betty-doc.pl
- You are not allowed to use global variables
- No more than 5 functions per file
- In the following examples, the main.c files are shown as examples. You can use them to test your functions, but you don’t have to push them to your repo (if you do we won’t take them into account). We will use our own main.c files at compilation. Our main.c files might be different from the one shown in the examples
- The prototypes of all your functions should be included in your header file called lists.h
- Don’t forget to push your header file
- All your header files should be include guarded

#Tasks#
*0. Print a list of integers* mandatory
Write a function that prints all integers of a list.

Prototype: def print_list_integer(my_list=[]):
Format: one integer per line. See example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use str.format() to print integers

GitHub repository: alx-higher_level_programming
Directory: 0x03-python-data_structures
File: 0-print_list_integer.py
   
*1. Secure access to an element in a list* mandatory
Write a function that retrieves an element from a list like in C.

Prototype: def element_at(my_list, idx):
If idx is negative, the function should return None
If idx is out of range (> of number of element in my_list), the function should return None
You are not allowed to import any module
You are not allowed to use try/except

GitHub repository: alx-higher_level_programming
Directory: 0x03-python-data_structures
File: 1-element_at.py
   
*2. Replace element* mandatory
Write a function that replaces an element of a list at a specific position (like in C).

Prototype: def replace_in_list(my_list, idx, element):
If idx is negative, the function should not modify anything, and returns the original list
If idx is out of range (> of number of element in my_list), the function should not modify anything, and returns the original list
You are not allowed to import any module
You are not allowed to use try/except

GitHub repository: alx-higher_level_programming
Directory: 0x03-python-data_structures
File: 2-replace_in_list.py
   
*3. Print a list of integers... in reverse!* mandatory
Write a function that prints all integers of a list, in reverse order.

Prototype: def print_reversed_list_integer(my_list=[]):
Format: one integer per line. See example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use str.format() to print integers

GitHub repository: alx-higher_level_programming
Directory: 0x03-python-data_structures
File: 3-print_reversed_list_integer.py
   
*4. Replace in a copy* mandatory
Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).

Prototype: def new_in_list(my_list, idx, element):
If idx is negative, the function should return a copy of the original list
If idx is out of range (> of number of element in my_list), the function should return a copy of the original list
You are not allowed to import any module
You are not allowed to use try/except

GitHub repository: alx-higher_level_programming
Directory: 0x03-python-data_structures
File: 4-new_in_list.py
   
*5. Can you C me now?* mandatory
Write a function that removes all characters c and C from a string.

Prototype: def no_c(my_string):
The function should return the new string
You are not allowed to import any module
You are not allowed to use str.replace()

GitHub repository: alx-higher_level_programming
Directory: 0x03-python-data_structures
File: 5-no_c.py
   
*6. Lists of lists = Matrix* mandatory
Write a function that prints a matrix of integers.

Prototype: def print_matrix_integer(matrix=[[]]):
Format: see example
You are not allowed to import any module
You can assume that the list only contains integers
You are not allowed to cast integers into strings
You have to use str.format() to print integers

GitHub repository: alx-higher_level_programming
Directory: 0x03-python-data_structures
File: 6-print_matrix_integer.py
   
*7. Tuples addition* mandatory
Write a function that adds 2 tuples.

Prototype: def add_tuple(tuple_a=(), tuple_b=()):
Returns a tuple with 2 integers:
The first element should be the addition of the first element of each argument
The second element should be the addition of the second element of each argument
You are not allowed to import any module
You can assume that the two tuples will only contain integers
If a tuple is smaller than 2, use the value 0 for each missing integer
If a tuple is bigger than 2, use only the first 2 integers

GitHub repository: alx-higher_level_programming
Directory: 0x03-python-data_structures
File: 7-add_tuple.py
   
*8. More returns!* mandatory
Write a function that returns a tuple with the length of a string and its first character.

Prototype: def multiple_returns(sentence):
If the sentence is empty, the first character should be equal to None
You are not allowed to import any module

GitHub repository: alx-higher_level_programming
Directory: 0x03-python-data_structures
File: 8-multiple_returns.py
   
*9. Find the max* mandatory
Write a function that finds the biggest integer of a list.

Prototype: def max_integer(my_list=[]):
If the list is empty, return None
You can assume that the list only contains integers
You are not allowed to import any module
You are not allowed to use the builtin max()

GitHub repository: alx-higher_level_programming
Directory: 0x03-python-data_structures
File: 9-max_integer.py
   
*10. Only by 2* mandatory
Write a function that finds all multiples of 2 in a list.

Prototype: def divisible_by_2(my_list=[]):
Return a new list with True or False, depending on whether the integer at the same position in the original list is a multiple of 2
The new list should have the same size as the original list
You are not allowed to import any module

GitHub repository: alx-higher_level_programming
Directory: 0x03-python-data_structures
File: 10-divisible_by_2.py
   
*11. Delete at* mandatory
Write a function that deletes the item at a specific position in a list.

Prototype: def delete_at(my_list=[], idx=0):
If idx is negative or out of range, nothing change (returns the same list)
You are not allowed to use pop()
You are not allowed to import any module

GitHub repository: alx-higher_level_programming
Directory: 0x03-python-data_structures
File: 11-delete_at.py
   
*12. Switch* mandatory
Complete the source code in order to switch value of a and b

You can find the source code here
Your code should be inserted where the comment is (line 4)
Your program should be exactly 5 lines long

GitHub repository: alx-higher_level_programming
Directory: 0x03-python-data_structures
File: 12-switch.py
   
*13. Linked list palindrome* mandatory
Technical interview preparation:

You are not allowed to google anything
Whiteboard first
Write a function in C that checks if a singly linked list is a palindrome.

Prototype: int is_palindrome(listint_t **head);
Return: 0 if it is not a palindrome, 1 if it is a palindrome
An empty list is considered a palindrome

GitHub repository: alx-higher_level_programming
Directory: 0x03-python-data_structures
File: 13-is_palindrome.c, lists.h
   
*14. CPython #0: Python lists* #advanced
CPython is the reference implementation of the Python programming language. Written in C, CPython is the default and most widely used implementation of the language.
Since we now know a bit of C, we can look at what is happening under the hood of Python. Let’s have fun with Python and C, and let’s look at what makes Python so easy to use.

All your files will be interpreted/compiled on Ubuntu 14.04 LTS


Create a C function that prints some basic info about Python lists.

Prototype: void print_python_list_info(PyObject *p);
Format: see example
Python version: 3.4
Your shared library will be compiled with this command line: gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
OS: Ubuntu 14.04 LTS
Start by reading:
- listobject.h
- object.h
- Common Object Structures
- List Objects

GitHub repository: alx-higher_level_programming
Directory: 0x03-python-data_structures
File: 100-print_python_list_info.c
