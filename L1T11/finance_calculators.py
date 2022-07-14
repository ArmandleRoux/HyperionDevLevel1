# Import math module for use of math.pow()
import math

# Request input from user to choose an option from the menu.
user_choice = input("Choose either 'Investment' or 'Bond' from the menu below" +
                    " to proceed: \n\n" +
                    "Investment \t - to calculate the amount of interest" +
                    " you'll earn on interest \n" +
                    "Bond       \t - to calculate the amount you'll have to" +
                    "to pay on a home loan \n\n>").lower()
 
print("-"*80)

# While loop to keep asking for infromation if menu option is invalid
while True:
    
    # Check user input to see if they want a loan or to invest and ask for the
    # appropriate information.
    if user_choice == "investment":
    
        # Request input from user to provide details of the investment.
        # Check the interest_type provided by user to determine which formulae
        # to use for end_total calculation.
        # Calculate the end_total using given information and print
        # results to console.
        deposit_amount = float(input("Enter the Amount you" +
                                     " are depositing: \n>"))
        print("-"*80)
        interest_rate = float(input("Enter your Interest rate: " +
                                    "(You only have to provide the number)\n>")
                              .replace("%" , ""))/100
        print("-"*80)
        time_period = int(input("Enter the amount of Years you are investing:"+
                                "\n>"))
        print("-"*80)
        interest_type = input("Would you like Simple or Compound interest?" +
                              "\n>").lower()
        print("-"*80)

        # While loop to keep asking for infromation if some
        # Interest type is invalid
        while True:
            if interest_type == "simple":
                end_total = round(deposit_amount *
                                  (1 + interest_rate * time_period), 2)
                total_interest = round(end_total - deposit_amount, 2)
                print(f"Amount Invested:           \t R{deposit_amount} \n" +
                      f"Interest Rate:             \t {interest_rate*100}% \n"+
                      f"Investment period:         \t {time_period} years \n" +
                      "*"*80 +              
                      f"\nTotal Interest Received: \t R{total_interest} \n" +
                      f"Investment end total:      \t R{end_total} \n" +
                      "*"*80)
                break
            elif interest_type == "compound":
                end_total = round(deposit_amount * math.pow((1 + interest_rate),
                                                            time_period), 2)
                total_interest = round(end_total - deposit_amount, 2)
                print(f"Amount Invested:           \t R{deposit_amount} \n" +
                      f"Interest Rate:             \t {interest_rate*100}% \n" +
                      f"Investment period:         \t {time_period} years \n" +
                      "*"*80 +           
                      f"\nTotal Interest Received: \t R{total_interest} \n" +
                      f"Investment end total:      \t R{end_total} \n" +
                      "*"*80)
                break
            else:
                print("Invalid Interest type!")
                interest_type = input("Please choose 'Simple'" +
                                      " or 'Compound'\n").lower()
                print("-"*80)
        break

    elif user_choice == "bond":
    
        # Request input from user to provide details for home loan/bond.
        # Calculate montly back payment for user using given information and
        # print results to console.
        house_value = float(input("Please enter the Value of the house: \n>"))
        print("-"*80)
        interest_rate = float(input("Enter your Interest rate:" +
                                    " (You only have to provide the number)" +
                                    "\n>")
                          .replace("%" , ""))/100
        print("-"*80)
        monthly_interest_rate = interest_rate/12
        time_period = int(input("How many Months will you take to" +
                                " repay this loan? \n>"))
        print("-"*80)

        monthly_payment = round((monthly_interest_rate * house_value)/
                            (1 - math.pow((1 + monthly_interest_rate),
                                          (-time_period))), 2)
        end_total = round(monthly_payment * time_period, 2)
    
        print(f"House value:             \t R{house_value} \n" +
              f"Interest Rate:           \t {interest_rate*100}% \n" +
              f"Pay Back Period:         \t {time_period} months \n" +
              "*"*80 +
              f"\nMonthly Payment:       \t\t R{monthly_payment} \n" +
              f"Total money to pay back: \t R{end_total}\n" +
              "*"*80)
        break

    else:
        # Print to console error message telling user they have not
        # selected a valid option
        print("This option is not on the menu!")
        user_choice = input("Please choose 'Investment' or 'Bond: \n").lower()
        print("-"*80)
            

