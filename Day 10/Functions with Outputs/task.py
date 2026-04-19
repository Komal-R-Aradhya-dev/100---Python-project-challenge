# def format_name(f_name,l_name):
#     f_name.title()
#     l_name.title()
#     return f"{f_name} {l_name}"
# full_naam= format_name(l_name = "Aradhya",f_name = "Komal")
# print(full_naam)
def my_function(a):
    if a < 40:
        return "Terrible"
    if a < 80:
        return "Pass"
    else:
        return "Great"
print(my_function(25))