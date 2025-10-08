# Age_checker Function Design Recipe

This is a recepie for age_checker function

## 1. Describe the Problem

```
As an admin
So that I can determine whether a user is old enough
I want to allow them to enter their date of birth as a string in the format `YYYY-MM-DD`.

As an admin
So that under-age users can be denied entry
I want to send a message to any user under the age of 16 saying their access is denied
And telling them their current age and the required age (16).

As an admin
So that old enough users can be granted access
I want to send a message to any user aged 16 or older to say that access has been granted.

```

## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def age_checker(dob):
    """Grants access based on age

    Parameters: (list all parameters and their types)
        dob: a string containing date of birth in format (e.g. "YYYY-MM-DD")

    Returns: (state the return value and its type)
        a string statement "Access granted!" or "Access denied"

    Side effects: (state any side effects)
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given the correct dob format 1997-12-10
It returns Access granted!
"""
age_checker("1997-12-10") => "Access granted!"

"""
Given the correct dob format 2015-10-08
It returns Access denied!
"""
age_checker("2015-10-08") => Access denied!

"""
Given incorrect dob format 2015/12/25
It returns an exception saying Invalid date
"""
age_checker("2015/12/25") => Invalid date

"""
Given incorrect date for e.g. 2023-34-21
It returns string Invalid date
"""
age_checker("2023-34-21") => Invalid date
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE
from lib.age_checker import *
import pytest

"""
Given the correct dob format 1997-12-10
It returns Access granted!
"""
def test_correct_dob_returns_access_granted():
    assert age_checker("1997-12-10") == "Access granted!"

"""
Given the correct dob format 2015-10-08
It returns Access denied!
"""
def test_correct_dob_under_16_returns_access_denied():
    assert age_checker("2015-10-08") == "Access denied!"

"""
Given incorrect dob format 2015/12/25
It returns an exception saying Invalid date
"""
def test_incorrect_dob_format_raises_exception():
    with pytest.raises(Exception) as e:
        age_checker("2015/12/25")
    
    actual = str(e.value)

    assert actual == "Invalid date"

"""
Given incorrect date for e.g. 2023-34-21
It returns string Invalid date
"""
def test_incorrect_dob_raises_exception():
    with pytest.raises(Exception) as e:
        age_checker(""2023-34-21"")
    
    actual = str(e.value)

    assert actual == "Invalid date"
```

Ensure all test function names are unique, otherwise pytest will ignore them!
