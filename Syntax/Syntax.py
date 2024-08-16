# Comments are written with a hastag in the beginning of the line or 

"""
or for 
multi line 
comments you 
use three paranthesis
"""

"""
Data types 

there are 5 different data types
theres int / "integers" => whole numbers for example : 1 , 2 , 3 , 12 , 157 ...
then float / "floating point numbers" => numbers with a dot : 1.1 , 1.13 , 0.002 , 1213.1448747 ...
char / "characters" => single letters or symbols : "c" , 'f' , ':'
str / "strings" => mutiple letters or symbols : "Hello World!"
"""

""" 
to declare a variable you first write the name of the variable 
(- the name of a variable shouldbe chosen wisely and should be instantly understandable as to what the var is used for), 
after deciding on a name you write the assignment operator: "=" (equals) and then you assign a value example: 3
example_variable = 3
this is a var of type int

to make that more obvious theres something called type annotation which is a must in many other programming languages
but not needed in python for the code to run

however because you are learning from me, i will make you write code this way 

example_variable: int = 3

this type annotation should only happen in the declaration of variables or parameters (more to those later)
"""

"""
operators are used to handle operation such as adding/subtracting/multiplying or dividing numbers.

example operators thus are: + | - | * | /
these are called arithmetic operators cuz you do math stuff with em
there are more though.

Theres also comparisson operators,
examples would be: == | < | <= | > | >= 
for comparing if two values or variables are the same you have to use double equals: "==" because the single = is reserved
for assigning values.
"""

"""
In order to add logic to your code, we have so called if-statements 
if-statements are often used together with comparrison operators
"""

arbitary_variable_1: int = 1
arbitary_variable_2: int = 3

# Example if-statement
if arbitary_variable_1 >= arbitary_variable_2:
    print("Cock")

"""
To create an if-statement you first use the if keyword to initialize the if-statement then you give your argument
this could be a comparrisson check or a set value 

The code inside of an if statement only gets executes when the comparrisson gets evaluated as true.
In our example that would mean for the code to print "Cock" arbitary_variable_1 would need to be 
greater or equals to arbitary_variable_2


if you want to eval more arguments you can use the elif or else keyword these following code blocks only get triggered
when the one before them evaluates to false
"""
# Example if-statement with eilf and else
if arbitary_variable_1 > arbitary_variable_2:
    print("Cock")
elif arbitary_variable_1 == arbitary_variable_2:
    print("elif")
elif arbitary_variable_1 < arbitary_variable_2:
    print("new elif number of elifs isnt restricted but dont overdue takes up unnessecery space")
else:
    print("else statements dont have arguments they only get executed when everything else fails")


"""
functions are repeatable code blocks that get called by a certain name


for example the print() function that you know is built with many complex steps first reading the 
argument then writing the argument to the screen buffer then making the screen buffer read it 
and then letting it be displayed by a seperate screen display function

what i wanted to show with all this text is that functions can have much code which is very complex 
and long and we group it in functions to save us from the headache of rewriting all these lines 
when we need the same thing to be done again and again

a function consist of its name possible parameters and of course the code that gets executed when
the function is called
the most basic function is a greeting function were you can enter the name and it greets you with that name
"""

# Function definition and declaration
def greeting_func(name: str) -> None:
    print("Hello" , name)


def return_func(num: int) -> int:
    return num

number = return_func(4)
#number is now equal to 4

# Function call
greeting_func("Muri")
# OUTPUT: -> Hello Muri

"""
so to define a function you first write the def keyword shot for define
then you write the name of the function again same thing as for variables clear easily readable names ONLY
then ( ) where you can add parameters for this we need a name otherwise we dont know who to greet
after that add a : and then the code block follows in this case a single print function

to actually use the function you just writes its name fill in the parameters if any and then your code gets 
executed after running it.
"""

# Known functions : print(), input()

