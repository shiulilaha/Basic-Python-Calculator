# This function safely takes float value with error handling
def get_num(num):
    while True:
        x = input("Enter " + num + " num: ")
        try:
            return float(x)
        except:
            print ("Invalid number, try again!")

x = None   # This will store our ongoing result

# Main calculator loop 
while True:
    if x is None:
        x = get_num("first")    # Start a new calculation with a number
    # Ask for operator input
    y = input("enter an operator( +, -, *, /,% , ^) or any alphabet to start over, or '**' to exit: ")
    if y == '**':
            print("Terminating calculator")
            exit()
    if y.isalpha():
        print("Starting new calculation..")
        x = None    # Reset calculation
        continue

    z = get_num("second")   # Ask for second number
    
    # Perform the corresponding operation
    if y == "+":
        x = x+z
    elif y=="-":
        x = x-z
    elif y=="*":
        x = x*z
    elif y=="/" and z !=0:
        x = x/z
    elif y=="/" and z==0:
        print("Cannot divide by 0!")
        continue
    elif y=="%":
        x = x%z
    elif y=="^":
        x = x**z
    else:
        print("Operator invalid") 

    # Print result rounded to 4 decimal places
    print("= ", round(x, 4))    

