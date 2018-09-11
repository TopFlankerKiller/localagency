import re


def is_allowed_specific_char(string):
    charRe = re.compile("^[a-zA-Z ]+$")
    string = charRe.search(string)
    return bool(string)


def check_string(myString):
    if (is_allowed_specific_char(myString)):
        my_striped_string = myString.strip()
        my_titled_string = my_striped_string.title()
        return my_titled_string
    else:
        return "Please give a valid string!!!"




#myString = "Taxi driver"
#print(check_string(myString))
# print("This is the initial string:"+myString)
#
# striped_string=myString.strip()
# print("This is the striped string:"+striped_string)
#
# titled_string=striped_string.title()
# print("This is the titled string:"+titled_string)
#
# print(is_allowed_specific_char(titled_string))











# print(check_string(myString))