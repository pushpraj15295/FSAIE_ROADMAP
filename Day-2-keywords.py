# keyword - python is a case sensitive programming language. 
# so we have to use the keywords in lower case only.
#  if we use any keyword in upper case then it will be treated as a variable name.
#. pythin has 35 keywords in total.

import keyword
print(keyword.kwlist) 
 
#  [ False, None, True, and, as, assert, async, await, break,
#  class, continue, def, del, elif, else, except, finally, for, 
#  from, global, if, import, in, is, lambda, nonlocal, not, or, pass, 
#  raise, return, try, while, with , yield ]


# -------------------------------------------------------------------------
# Identifiers - Identifiers are the names given to entities like class, functions, variables, etc. 
# It helps to differentiate one entity from another.

# example of valid identifiers in python:
# my_variable
# myVariable
# _my_variable  
#  _ 
#  __


# example of invalid identifiers in python: [ invalid - you will get syntax error if you use these identifiers ]
# 1my_variable
# my-variable
# my variable
# my@variable  