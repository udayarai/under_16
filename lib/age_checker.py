from datetime import datetime, date

def age_checker(dob):
    try:
        dob_object = datetime.strptime(dob, "%Y-%m-%d").date()
    except ValueError:
        raise Exception("Invalid date")
    
    current_date = date.today()

    had_birthday_this_year = (dob_object.month, dob_object.day) < (current_date.month, current_date.day)
    
    if had_birthday_this_year:
        age = current_date.year - dob_object.year 
    else:
        age = current_date.year - dob_object.year - 1

    if age >= 16:
        return "Access granted!"
    else:
        return "Access denied!"
    




