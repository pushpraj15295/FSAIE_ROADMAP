# Generic and Static Reasoning in Python    

# Generic reasoning is a way to reason about code that can handle different types of data.

import typing as tp

def get_first(items: tp.List[tp.Any]) -> tp.Any:
    return items[0]

print(get_first([10, 20, 30]))
print(get_first(["Pushpraj", "Rahul"])) 





# What is static type checking?  ------------------------------------------------------------------
# You probably mean static type checking by “static reasoning.”


# Static type checking means analyzing code for type-related problems
#  without executing the program. A type checker examines your annotations 
# and how values are used to identify possible mistakes.

