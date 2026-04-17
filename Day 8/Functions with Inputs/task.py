def greet():
    print("Hello World")
    print("How are you?")
    print("How are you doing?")
greet()

def greet_with_name(name):
    print(f"Hello, {name}!")
    print("How are you?")
    print("How are you doing?")
name = input("Enter your lovely name:\n")
greet_with_name(name)