#
#
# try:
#     result=10/0
#
# except ZeroDivisionError:
#     print("Oops, cant divide by zero!")
#
#
#
# fruits = {
#     "apple": 5,
#     "Orange": 6,
#     "milot rrushi": 3
# }
#
# try:
#     print(fruits["chery"])
#
# except KeyError:
#     print("The key does not match")
#
#
# text ="this is not a number"
#
# try:
#     text_to_int = int(text)
#
# except Exception as e:
#     print("an error occurred", e)
#
# try:
#     result = 10/2
# except ZeroDivisionError:
#     print("division by 0")
# else:
#     print("division success, reult:", result)
#
# try:
#     result = 10/0
# except ZeroDivisionError:
#     print("we have an error")
# finally:
#     print("executed")
#
# def divide_numbers(a,b):
#     try:
#         result = a/b
#         print("the result is:", result)
#     except ZeroDivisionError:
#         print("You tried to divide by 0")
#     except TypeError:
#         print("Invalid type for division")
#     except Exception as e:
#         print("Unexpected error", e)
#
# divide_numbers(10, 2)
# divide_numbers(10, 0)
# divide_numbers(10, '2')





def miloti(a,b, operator):
   if operator == "+":
       return  a + b
   elif operator == "-":
       return  a - b
   elif operator == "*":
       return  a *  b
   elif operator == "/":
       return  a / b
   else:
       raise ValueError("invalid op")
try:
    a = float(input("type number 1"))
    b = float(input("type number 2"))
    operator = input("enter an operation: ")
    result = miloti(a, b, operator)
    print("the result of operation is", result)
except ValueError:
    print("Invalid input")
except ZeroDivisionError:
    print("cant divide by 0")
except Exception as e:
    print("there was an error", e)
finally:
    print("code was exec")
