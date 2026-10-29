# Optional and Union Type Hinting in Python

# Sometimes a variable may contain a value, or it may contain None.
# Optional[str] means str or None. The str | None form needs Python 3.10+.

from typing import Optional, Union

def get_note() -> Optional[str]:
    return None

note = get_note()

if note is not None:
    print(note.upper())
else:
    print("No note provided")


# Union[int, str] means the value can be an int or a str.
def get_code() -> Union[int, str]:
    return 10

print(get_code())

# Important: Optional[str] does not mean the argument is optional to provide.
#  It means its value may be None. Whether an argument can be omitted depends on its default value.


# What is Union? --------------------------------------------------------------
# Union means a value can be one of several specified types.

def display_amount(amount: int | float | str) -> None:
    print(amount)

display_amount(500)
display_amount(500.50)
display_amount("500")

# All three calls are valid according to the type hint.
# ----------------------------------------------------------------------------


