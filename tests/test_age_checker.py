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
        age_checker("2023-34-21")
    
    actual = str(e.value)

    assert actual == "Invalid date"