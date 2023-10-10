
choice = input('Which function would you like to use? \n 1: GetChildren \n 2: ChangeDiscount \n answer: ')

if choice  == '1':
    parameter = input("Enter the Department ID: ")
    GetChildren(parameter)
if choice == '2': 
    parameter = input("Enter the Product ID: ")
    ProductID(parameter)

