# Request user input to provide a year and an amount of years afterward.
# Calculate end_year using total_years input provided
start_year = int(input("Enter a year to start leap year calculation: \n"))
print("-"*80)
total_years = int(input("How many year ahead would you like to know? \n"))
end_year = start_year + total_years
print("-"*80)

print("*"*26)
# Calculate if the years from the start_year and the total_years after it
# is or was a leap year and print result to console
for year in range(start_year, end_year):
    if year%4 == 0:
        print(f"*{year} is a leap year!    *")
    else:
        print(f"*{year} is not a leap year.*")
        
print("*"*26)
