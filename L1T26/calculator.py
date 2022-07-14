'''Defined a function that takes 2 numbers and an operator asarguments. 
Calculate the result between the 2 numbers with the given operator and 
return result.'''
def equate(num1, num2, symbol):   
    if symbol == "+":
        return num1 + num2
    elif symbol == "-":
        return num1 - num2
    elif symbol.lower() == "x":
        return num1 * num2
    elif symbol == "/":
        return round(num1 / num2, 2)


'''Main loop of program. 
Request user input to choose an option from the menu.
-If user chooses to add an equation. Request input from user to provide a name
 for the file they wish to save the equations to, 2 numbers and an operator
 write equations to file with specified name. Ask user if they want to add 
 another equation or to go back to main menu.

-If user chooses to see results of equations request input from provide the 
name of the file with the equations they wish to display. If file doesn't
exist  request name from user again. Open the file and readall lines and 
split the data in each line to a list. Read the data into equate() funtion 
to calculate results. Print equations with results to console.

-If user enters "0" program will stop

-If no option is selected print error message to console and prompt menu 
again'''
while True:
    print("-"*80)
    menu = input("Choose an option below:\n"
                "1 - Add Equation\n" 
                "2 - See Results of all Equations\n"
                "0 - Quit\n>")
    
    print("-"*80)
    if menu == "1":
        user_eq_file = input("Enter the name of the file you would like"
                             " to store your equations in: \n>")
        print("-"*80)
        if ".txt" not in user_eq_file:
            user_eq_file += ".txt"
        while True:
            while True:
                try:
                    user_num1 = int(input("Enter a number: \n>"))
                    print("-"*80)
                    break
                except ValueError:
                    print("Oops! That was not a valid number. Try again...")
                    print("-"*80)
                    
            while True:
                try:
                    user_num2 = int(input("Enter a another number: \n>"))
                    print("-"*80)
                    break
                except ValueError:
                    print("Oops! That was not a valid number. Try again...")
                    print("-"*80)
            user_symbol = input("What would you like to do with the numbers?"
                                "\n(+,-,x,/)\n>")
            print("-"*80)
            while user_symbol not in "+-*/":
                user_symbol = input("Oops looks like you didn't choose one of"
                                    " the options:\nTry again: (+,-,*,/)\n>")
                print("-"*80)
                
            with open(user_eq_file, "a") as eq_file:
                eq_file.write(f"{user_num1} {user_symbol} {user_num2}\n")

            print(f"Your Equation was Added to {user_eq_file}:\n"
                f"{user_num1} {user_symbol} {user_num2}")
            print("-"*80)
            user_choice = input("If you would like to go back to menu type "
                                "'0'.\nPress enter to do another equation.\n")
            if user_choice == "0":
                print("Equations Saved!")
                break
    
    elif menu == "2":
        user_file = ""
        while True:
            user_file = input("Enter the name of your equation file:\n"
                              "(Type 0 to go back)\n>")           
            if user_file == "0":
                break
            if ".txt" not in user_file:
                user_file += ".txt"
            try:
                with open(user_file, "r") as eq_file:
                    print("-"*80)
                    print("Equations: \n")
                    for line in eq_file:
                        data = line.replace("\n", "")
                        data = data.split(" ")
                        try:
                            print(f"{data[0]} {data[1]} {data[2]} = " +
                                str(equate(int(data[0]), int(data[2]),
                                        data[1])))
                        except ValueError:
                            print("One or more equation in the file is "
                                "in the wrong format.")
                break
            except FileNotFoundError:
                print("-"* 80)
                print("File not found. Try Again.")
    
    elif menu == "0":
        break
    
    else:
        print("No option selected!")
