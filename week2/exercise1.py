"""
Commenting skills:

TODO: above every line of code comment what you THINK the line below does.
TODO: execute that line and write what actually happened next to it.

See example for first print statement
"""

# I think it will implement many things 
import platform #

# I think this will print "hello! Let's get started" by calling the print function.
print("hello! Let's get started")  # it printed "hello! Let's get started"

# I think this will assign some_words to a list of strings. 
some_words = ['what', 'does', 'this', 'line', 'do', '?'] #

# I think it will print each word in a list.
for word in some_words:
    print(word) #It printed each word in the list in a list 

# I think it will do the exact same as the code above, as it does not matter what the variable is.
for x in some_words:
    print(x) # it printed the exact same thing as the code above

# I think it will print the list 
print(some_words) # It printed ['what', 'does', 'this', 'line', 'do', '?']

# I think if there are more 3 words in some_words then it will print 'some_words contains more than 3 words'
if len(some_words) > 3:
    print('some_words contains more than 3 words') # it printed 'some_words contains more than 3 words'

# I think it defines a function as usefulFunction 
def usefulFunction():
    """
    You may want to look up what uname does before you guess
    what the line below does:
    https://docs.python.org/3/library/platform.html#platform.uname
    """
    # I think it will print informatiion of the platform returning the system, node, release, version, machine, and processor.
    print(platform.uname()) # It printed information about the system, node, release, version, machine, and processor.

usefulFunction()
