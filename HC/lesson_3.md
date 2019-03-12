# Lesson 3
## Functions, Parameters, and Return Values

### Functions
#### Defining

A function in Python is defined with the def keyword. Functions do not have declared return types. A function without an explicit return statement returns None. In the case of no arguments and no return value, the definition is very simple.

Calling the function is performed by using the call operator () after the name of the function.

```python
>>> def hello_function():
...     print 'Hello World, it\'s me.  Function.'
...

>>> hello_function()
Hello World, it's me.  Function.
```

#### Arguments
The arguments of a function are defined within the def statement. Like all other variables in Python, there is no explicit type associated with the function arguments. This fact is important to consider when making assumptions about the types of data that your function will receive.

Function arguments can optionally be defined with a default value. The default value will be assigned in the case that the argument is not present in the call to the function. All arguments without default values must be listed before arguments with default values in the function definition.

Any argument can be passed either implicitly by position or explicitly by name, regardless of whether or not it has a default value defined.

```python
>>> def record_score(name, score=0):
...     print '%s scored %s' % (name, score)
...

>>> record_score('Jill', 4)
Jill scored 4

>>> record_score('Jack')
Jack scored 0

>>> record_score(score=3, name='Pail')
Pail scored 3

>>> record_score(2)
2 scored 0

>>> record_score(score=2)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  TypeError: record_score() takes at least 1 non-keyword argument (0 given)

>>> record_score()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  TypeError: record_score() takes at least 1 argument (0 given)
```

Note
Look carefully at the example above. There is an asymmetry in the use of the = sign for defining vs. passing arguments that can be confusing to beginners. An argument with a default value can be passed using only position and an argument without a default can be passed using a keword.


 Scope
Each function evaluation creates a local namespace that is manipulated at any level within the function. As a result, variables can be initially defined at a seemingly lower level of scope than they are eventually used.
```python
>>> def deep_scope():
...     if True:
...         if True:
...             if True:
...                 x = 5
...     return x
...

>>> deep_scope()
5
```

Warning
This model for scope can simplify your code, but pay attention. If you don’t anticipate all code paths, you can end up referencing undefined variables.
```python
>>> def oops(letter):
...     if letter == 'a':
...         out = 'A'
...     return out
...

>>> oops('a')
'A'

>>> oops('b')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in oops
UnboundLocalError: local variable 'out' referenced before assignment
```

## Exception Handling

Errors and Exceptions

Until now error messages haven’t been more than mentioned, but if you have tried out the examples you have probably seen some. There are (at least) two distinguishable kinds of errors: syntax errors and exceptions.

8.1. Syntax Errors

Syntax errors, also known as parsing errors, are perhaps the most common kind of complaint you get while you are still learning Python:
```python
>>>
>>> while True print('Hello world')
  File "<stdin>", line 1
    while True print('Hello world')
                  ^
SyntaxError: invalid syntax
```
The parser repeats the offending line and displays a little ‘arrow’ pointing at the earliest point in the line where the error was detected. The error is caused by (or at least detected at) the token preceding the arrow: in the example, the error is detected at the function print(), since a colon (':') is missing before it. File name and line number are printed so you know where to look in case the input came from a script.

8.2. Exceptions

Even if a statement or expression is syntactically correct, it may cause an error when an attempt is made to execute it. Errors detected during execution are called exceptions and are not unconditionally fatal: you will soon learn how to handle them in Python programs. Most exceptions are not handled by programs, however, and result in error messages as shown here:
```python
>>>
>>> 10 * (1/0)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
>>> 4 + spam*3
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'spam' is not defined
>>> '2' + 2
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
TypeError: Can't convert 'int' object to str implicitly
```
The last line of the error message indicates what happened. Exceptions come in different types, and the type is printed as part of the message: the types in the example are ZeroDivisionError, NameError and TypeError. The string printed as the exception type is the name of the built-in exception that occurred. This is true for all built-in exceptions, but need not be true for user-defined exceptions (although it is a useful convention). Standard exception names are built-in identifiers (not reserved keywords).

The rest of the line provides detail based on the type of exception and what caused it.

The preceding part of the error message shows the context where the exception happened, in the form of a stack traceback. In general it contains a stack traceback listing source lines; however, it will not display lines read from standard input.

Built-in Exceptions lists the built-in exceptions and their meanings.

8.3. Handling Exceptions

It is possible to write programs that handle selected exceptions. Look at the following example, which asks the user for input until a valid integer has been entered, but allows the user to interrupt the program (using Control-C or whatever the operating system supports); note that a user-generated interruption is signalled by raising the KeyboardInterrupt exception.

```python
>>>
>>> while True:
...     try:
...         x = int(input("Please enter a number: "))
...         break
...     except ValueError:
...         print("Oops!  That was no valid number.  Try again...")
...
```
The try statement works as follows.

First, the try clause (the statement(s) between the try and except keywords) is executed.

If no exception occurs, the except clause is skipped and execution of the try statement is finished.

If an exception occurs during execution of the try clause, the rest of the clause is skipped. Then if its type matches the exception named after the except keyword, the except clause is executed, and then execution continues after the try statement.

If an exception occurs which does not match the exception named in the except clause, it is passed on to outer try statements; if no handler is found, it is an unhandled exception and execution stops with a message as shown above.

## Global Variables/Constants
### Scope

```python
Each function evaluation creates a local namespace that is manipulated at any level within the function. As a result, variables can be initially defined at a seemingly lower level of scope than they are eventually used.

>>> def deep_scope():
...     if True:
...         if True:
...             if True:
...                 x = 5
...     return x
...

>>> deep_scope()
5
```
Warning

This model for scope can simplify your code, but pay attention. If you don’t anticipate all code paths, you can end up referencing undefined variables.

```python
>>> def oops(letter):
...     if letter == 'a':
...         out = 'A'
...     return out
...

>>> oops('a')
'A'

>>> oops('b')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
  File "<stdin>", line 4, in oops
UnboundLocalError: local variable 'out' referenced before assignment
```

## Text Files
