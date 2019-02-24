# N.B. We will be using python 3

# BASIC DATA STRUCTURES

integer = 7
type(integer) # <class 'int'>

floating_number = 3.14
type(floating_number) # <class 'float'>

# STRINGs

double_quated_string = "I am a string"
type(string1) # <class 'str'>

single_quated_string = 'I am a string too'
type(string2) # <class 'str'>

char = 'g' 
type(char) # <class 'str'>, char does not exist

# backslashes for special characters 
tab_string = "\t" # tab character
len(tab_string) # is 1

# if you want backslashes as backslashes, create raw strings using r
not_tab_string = r"\t" # represents the character '\' and 't'
len(not_tab_string) # is 2

# can create multiline strings using triple-double quote ("""...""")
multi_line_string = """This is the first line.
and this is the second line
and this is the third line"""

# FUNCTIONS
# functions are first-class, which means that we can assign them to variables

def double(x):
	return x*2

def apply_to_one(f):
	return f(1)

my_double = double # refers to previously defined functions
x = apply_to_one(double) # equlas 2

# anonympous functions with lambda (it can be assigne to variable but always assign to functions)
y = apply_to_one(lambda x : x+4) # equals 5
# or #
another_double = lambda x : x*2 # don't do this
def another_double(x):
	return lambda x : x*2 # do this instead

# default arguments can also assigned to funcrions
def my_print(message="Hello, World!"):
	print(message)

my_print("Hello, Python!") # prints 'Hello, Python!'
my_print() # prints 'Hello, World!'

# can specify arguments by name
def subtract(a=0, b=0):
	return a-b

subtract(10, 5) # returns 5
subtract(0, 5) # returns -5
subtract(b=5) # same as previous

# EXCEPTIONS

try:
	print(0/0)
except ZeroDivisionError:
	print("cannot divide by zero")

# LISTS
# ordered collection - like an array but with added functionalities

integer_list = [1, 2, 3]
heterogeneous_list = ["string", 0.1, True]
list_of_lists = [integer_list, heterogeneous_list, []]

list_length = len(integer_list) # 3
list_sum = sum(integer_list) # 6

# you can get and set nth element of a list with square brackets
x = list(range(10)) # is the list [0, 1, ..., 9]
zero = x[0] # 0, lists are 0-indexed
one = x[1] # 1
nine = x[-1] # 9, 'Pythonic' for last element
eigth = x[-2] # 8, 'Pythonic' for next-to-last element
x[0] = -1 # now x is [-1, 1, 2, ..., 9]

# list slicing - recall x = [-1, 1, 2, ..., 8, 9]
first_three = x[:3] # [-1, 1, 2]
three_to_end = x[3:] # [3, 4, ..., 9]
one_to_four = x[1:5] # [1, 2, 3, 4]
last_three = x[-3:] # [7, 8, 9]
without_first_and_last = x[1:-1] # [1, 2, .., 8]
copy_of_x = x[:] # [-1, 1, 1, ..., 9]

# check membership
1 in [1, 2, 3] # True
0 in [1, 2, 3] # False
# N.B. same operations available for str type (strings)

# concatenate lists together
x = [1, 2, 3]
x.extend([4, 5, 6]) # x is now [1, 2, 3, 4, 5, 6]

# if you don't want to modify x you can use list addiction
x = [1, 2, 3]
y = x + [4, 5, 6] # y is [1, 2, 3, 4, 5, 6], x is unchanged

# can add (append) elements at the back of the list - one at the time
x = [1, 2, 3]
x.append(0) # x is now [1, 2, 3, 0]
x[-1] # 0, was 3
len(x) # 4, was 3

# lists can be unpacked if you know how many elements they contain
# will get ValueError if you don't have the same number of elements on both sides
x, y = [1, 2] # now x is 1 and y is 2

# underscore (_) a value you are ging to throw away
_, y = [1, 2] # now y is 2, didn't care about the first element

# TUPLES
# immutable lists

my_list = [1, 2]
my_tuple = (1, 2)
other_tuple = 3, 4
my_list[1] = 3 # my_list is now [1, 3]

try:
	my_tuple[1] = 3
except TypeError:
	print("Cannot modify tuple!")

# tuples are a way to return multiple values from a function
def sum_and_product(x, y):
	return (x+y), (x*y)

sp = sum_and_product(2, 3) # equals (5, 6)
s, p = sum_and_product(5, 10) # s is 15, p is 50

# tuples (and lists) can also be used for multiple assignemnts
x, y = 1, 2 # now x is 1, y is 2
x, y = y, x # 'Pythonic' way to swap variables; now x is 2, y is 1

# DICTIONARIES
# associates values with keys
# keys must be immutable; in particular, you cannot use lists as keys
# if you need a multipart key, you should use a tuple

empty_dict = {} # Pythonic
empty_dict2 = dict() # less Pythonic
grades = {"Gian" : 80, "Esraa" : 95} # dictionary literal

# value can be looked up using square brackets
gian_grade = grades["Gian"] # equals 80

# KeyError if you ask for a key that it is not in the dictionary
try:
	kates_grades = grades["Kate"]
except KeyError:
	print("no grades for that student")

# can check existence of a key
gian_has_grade = "Gian" in grades # True
kate_has_grade = "Kate" in grades # False

# dicts have a get method that return a default value (instead of raising an exception) 
# get(key, default=None)
gian_grade = grades.get("Joel", 0) # 80
kate_grade = grades.get("Kate", 0) # 0
no_ones_grade = grades.get("No One") # default is None - get("key", None)

# can assign key-value using the same square bracket
grades["Tim"] = 99 # replace the old value
grades["Kate"] = 100 # add a third entry
num_students = len(grades) # equals 3

# use dicts as a simple way to represent structured data
student = {
	"user" : "gripepi",
	"text" : "CS student",
	"avg_grade" : 100,
	"active_modules" : ["IN3001", "IN3029", "IN3045", "IN3006"]
}

# besides of looking at specific keys, we can look at all of them
student_keys = student.keys() # list of keys
student_values = student.values() # list of values
student_items = student.items() # list of (key, value) tuples

"user" in student_keys # True, but uses a slow list in
"user" in student # more 'Pythonic', uses faster dict in
"gripepi" in student_values # True

# SETS
# collection of distinct elements

s = set()
s.add(1) # s is now { 1 }
s.add(2) # s is now { 1, 2 }
s.add(2) # s is now { 1, 2 }
x = len(s) # 2
y = 2 in s # True
z = 3 in s # False

# in is a very fast opereation on sets (hundreds_of_other_word not declare but imagine it contains 100 words)
stopwords_list = ["a", "an", "at"] + hundreds_of_other_word + ["yet", "you"]

"zip" in stopwords_list # False, but have to check every element

stopwords_set = set(stopwords_list)
"zip" in stopwords_set # very fast to check

# second reason is to find the DISTINCT elements in a collection
item_list = [1, 2, 3, 1, 2, 3]
num_items = len(item_list) # 6
item_set = set(item_list) # { 1, 2, 3 }
num_distinct_items = len(item_set) # 3
distinct_item_list = list(item_set) # [1, 2, 3]

# CONTROL FLOW

# if statements
if 1 > 2:
	message = "if only 1 were greater than two..."
elif 1 > 3:
	message = "elif stands for 'else if'"
else:
	message = "when all else fails use else (if you want to)"

# ternary if-then-else (all on one line)
parity = "even" if x%2 == 0 else "odd"

# while loop
x = 0
while x < 10:
	print(x, "is less than 10")
	x += 1

# for and in loop - range is exclusive and can also take 2 arguments (start, end)
for x in range(10):
	print(x, "is less than 10")

# for more complex logic, continue and break can be used
for x in range(10):
	if x == 3:
		continue # go immediately to the next iteration
	if x == 5:
		break # quit the loop entirely
	print(x) # 1, 2, 4

# MODULES AND FUNCTOOLS

# to use modules use keyword import
import functools

# modules can be given an alias using keyword as
import functools as first_three

# can also import only the part of a module using keyword from
from functools import partial, reduce

def exp(base, power):
	return base**power # want to use this function to create two_to_the function

# we can use this
def two_to the(power):
	return exp(2, power) # this can get unwiedly

two_to_the = partial(exp, 2) # it is a new fuction of one variable
print(two_to_the(3)) # 8
# or
square_of = partial(exp, power=2) # you can specify the argument name and specify the rest later
print(square_of(3)) # 9

# other functional tools are: map, reduce, filter - which provide alternatives to list comprehensions
# map
def double(x):
	return 2*x

xs = [1, 2, 3, 4]
twice_xs = [double(x) for x in xs] # [2, 4, 6, 8]
twice_xs = map(double, xs) # same as above
list_doubler = partial(map, double) # *function* that doubles a list
twice_xs = list_doubler(xs) # again [2, 4, 6, 8]

# map can have multiple arguments if you provide multiple lists
def multiply(x, y):
	return x*y

products = map(multiply, [1, 2], [4, 5]) # [1*4, 2*5] = [4, 10]

# filter does the work of list-comprehensions if
def is_even(x):
	return x%2 == 0

x_evens = [x for x in xs if is_even(x)] # [2, 4]
x_evens = filter(is_even, xs) # same as above
list_evener = partial(filter, is_even) # *function* that filters a list
x_evens = list_evener(xs) # again [2, 4]

# reduce combines the first two elements of a list, then the result with the third,
# that result with the fourth, and so on, producing a single result 
# from functools import partial, reduce - has to be imported from functools

x_product = reduce(multiply, xs) # = 1*2*3*4 = 24
list_product = partial(reduce, multiply) # *function* that reduces a list
x_product = list_product(xs) # again = 24