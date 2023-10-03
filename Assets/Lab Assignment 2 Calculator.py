#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Yosif Iskander #100851999
# Infinte loop
memory = 0.0
loop = 'yes'
while loop == 'yes':
    function = '1'
    while function != 'add' and function != '+' and function != 'subtract' and function != '-' and function != 'multiply' and function != '*' and function != 'divide' and function != '/' and function != 'raise' and function != '^' and function != 'exit' and function != 'stop':
                        # for some reason or was not working so i decided to use and then it worked
# Select + - / or ^
        print("1. Enter Add or +",'\n' + "2. Enter Subtract or -",'\n' + "3. Enter Multiply or *",'\n' + "4. Enter Divide or /",'\n' "5. Enter Raise or ^",'\n' + "6. Enter Exit or Stop")

    # Acquire Inputs
        function = input("Please select from the following Functions: ").lower()
        print("")
    print('\n' + function)
    if (function == "stop" or function == "exit"):
        print("Stopping Calculator,",'\n' + "Good Bye")
        break
    x = input("Enter First Value: ")
    if (x == "stop" or x == "exit"):
        print("Stopping Calculator,",'\n' + "Good Bye")
        break
    y = input("Enter Second Value: ")
    if (y == "stop" or y == "exit"):
        print("Stopping Calculator,",'\n' + "Good Bye")
        break
#Calculate Functions
    oneval = False
    if (x == ""):
        x = y
        oneval = True
    elif (y == ""):
        oneval = True
    if not oneval:
        y = float(y)
    x = float(x)
    if (function == "add" or function == "+"):    
        if oneval:
            result = memory + x
        else:
            result = x+y
    elif (function == "subtract" or function == "-"):
        if oneval:
            result = memory - x
        else:
            result = x-y
    elif (function == "multiply" or function == "*"):
        if oneval:
            result = memory * x
        else:
            result = x*y
    elif (function == "divide" or function == "/"):
        if oneval:
            while x == 0:
                x = input("Can't divide by Zero Please re-enter value: ")
                if (x == "stop" or x == "exit"):
                    break
            if (x == "stop" or x == "exit"):
                print("Stopping Calculator,",'\n' + "Good Bye")
                break
            x = float(x)
            result = memory / x
        else:
            while y == 0:
                y = input("Can't divide by Zero Please re-enter value: ")
                if (y == "stop" or y == "exit"):
                    break
            if (y == "stop" or y == "exit"):
                print("Stopping Calculator,",'\n' + "Good Bye")
                break
            y = float(y)
            result = x/y
    elif (function == "raise" or function == "^"):
        if oneval:
            num = memory
            e = x
        else:
            num = x
            e = y
        counter = 0
        total = 1
        if (e >= 0):
            while counter < e:
                total *= num
                counter += 1
        else:
            while counter > e:
                total /= num
                counter -= 1
        result = total
    memory = result
    print("The Result is",result,'\n')


# In[ ]:




