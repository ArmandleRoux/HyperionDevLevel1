# Print to console a count down from 20 to 0
i = 20
while i >= 0:
    print(i)
    i -= 1

print("-"*80)

# Print to console all even numbers between 20 and 0
for num in range(1, 20):
    if num%2 == 0:
        print(num)

print("-"*80)

# Print a star patern to console where each line has an extra star up untill
# 5 stars
char = ""
for x in range(0, 5):
    char += "*"
    print(char)


print("-"*80)

# Decalred 2 positive integers and calculate greatest common divisor
# Print result to console
num1 = 18
num2 = 48

if num1 > num2:
    for y in range(num2, 0, -1):
        if num1%y == 0 and num2%y == 0:
            print(y)
            break
elif num2 > num1:
    for y in range(num1, 0, -1):
        if num1%y == 0 and num2%y == 0:
            print(y)
            break

