num1= input("Enter num1:")
num2= input("Enter num2:")

def devision(num1,num2):
    try:
        quotient=num1 / num2
        print(quotient)
    except ZeroDivisionError:
        print("Error:num2 cannot be aa zero")
    except TypeError:
        print("Error:Both num must be int or float")
    finally:
        print("Isn't division fun!")