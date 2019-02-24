# N.B. We will be using python 3

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