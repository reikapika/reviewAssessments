"""
Skills function assessment.

Please read the the instructions first (separate file). Your solutions should
go below this docstring.

PART ONE: Write your own function declaration - Part 1 questions aren't included in the doctest.

PART TWO:

    >>> is_berry("blackberry")
    True

    >>> is_berry("durian")
    False

    >>> shipping_cost("blackberry")
    0

    >>> shipping_cost("durian")
    5

    >>> is_hometown("Oakland")
    True

    >>> is_hometown("Chicago")
    False

    >>> full_name("Jane", "Hacker")
    'Jane Hacker'

    >>> hometown_greeting("Oakland", "Sarah", "Developer")
    "Hi Sarah Developer, we're from the same place!"

    >>> hometown_greeting("Chicago", "Jane", "Hacker")
    'Hi Jane Hacker, where are you from?'

    >>> append_to_list([3, 5, 7], 2)
    [3, 5, 7, 2]

PART THREE: Write your own function declarations - Part 3 questions aren't included in the doctest.

"""



# PART ONE


# 1. We have some code to calculate an item cost
#    by adding tax. Tax is normally 5% but it's higher in
#    California (7%).

#    Turn this code into a function. Your function will pass in
#    the default tax amount (5%), a state abbreviation, and the
#    cost amount as parameters.

#    If the state is California, apply a 7% tax within the function.
#    Your function should return the total cost of the item,
#    including tax.

#    If the user does not provide a tax rate it should default to 5%.

# NOTE: This function isn't included in the doctest, so make sure and test that it works.


#####################################################################
# PART TWO


# 1. (a) Write a function, `is_berry()`, which takes a fruit name as a string
#        and returns a boolean if the fruit is a "strawberry", "cherry", or
#        "blackberry".


def is_berry(fruit):
    """Determines if fruit is a berry"""
    pass

#    (b) Write another function, shipping_cost(), which calculates shipping cost
#        by taking a fruit name as a string, calling the `is_berry()` function
#        within the `shipping_cost()` function and returns 0 if ``is_berry()
#        == True``, and 5 if ``is_berry() == False``.


def shipping_cost(fruit):
    """Calculates shipping cost of fruit"""
    pass

# 2. (a) Write a function, `is_hometown()`, which takes a town name as a string
#        and evaluates to `True` if it is your hometown, and `False` otherwise.
#


def is_hometown(town):
    """Check whether town is hometown."""
    pass


#    (b) Write a function, `full_name()`, which takes a first and last name as
#        arguments as strings and returns the concatenation of the two names in
#        one string.


def full_name(first, last):
    """Construct full name from first and last."""
    pass

#
#    (c) Write a function, `hometown_greeting()`, which takes a home town, a
#        first name, and a last name as strings as arguments, calls both
#        `is_hometown()` and `full_name()` and prints "Hi, 'full name here',
#        we're from the same place!", or "Hi 'full name here', where are you
#        from?" depending on what `is_hometown()` evaluates to.


def hometown_greeting(town, first, last):
    """Output greeting that depends on hometown."""
    pass

# 3. Make a function that takes in a number and a list of numbers. It should append
#    the number to the list of numbers and return the list.


def append_to_list(lst, num):
    """Appends the given number to the end of the given list."""
    pass

#####################################################################
# PART THREE: ADVANCED
# NOTE: These functions aren't included in the doctest, so make sure to test them.


# 1. Make a new function that takes in any number of separate arguments, appends them to a list, and returns the entire list.

# 2. Make a new function with a nested inner function.
# The outer function will take in a word.
# The inner function will multiply that word by 3.
# Then, the outer function will call the inner function.
# Output will be the original function argument and the result of the inner function.
# Example:
#>>> outer("Balloonicorn")
#('Balloonicorn', 'BalloonicornBalloonicornBalloonicorn')


#####################################################################
# END OF ASSESSMENT: You can ignore everything below.

if __name__ == "__main__":
    import doctest

    print
    result = doctest.testmod()
    if not result.failed:
        print "ALL TESTS PASSED. GOOD WORK!"
    print
