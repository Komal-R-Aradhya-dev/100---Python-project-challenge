def calculator():
    global first_num
    global second_num
    global operator
    first_num = float(input("Enter  the first number?: "))
    print("+ \n"
          "- \n"
          "* \n"
          "/ \n")
    print("Enter your operator")
    operator = input()
    second_num = float(input("Whats the next number?:"))

    if operator == "+":
        return first_num + second_num
    elif operator == "-":
        return first_num - second_num
    elif operator == "*":
        return first_num * second_num
    elif operator == "/" and second_num != 0:
        return first_num / second_num
    elif operator == "%":
        return first_num % second_num
    else:
        return ("invalid input!")


result = calculator()
print(f"{first_num} {operator} {second_num} =  {result}")





