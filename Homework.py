num = int(input("Enter a number to check if it is an armstrong number: "))

num_str = str(num)
n = len(num_str)
total = 0

for digit in num_str:
    total += int(digit) ** n

if total == num:
    print(num, "is an Armstrong number.")
else:
    print(num, "is not an Armstrong number.")

if num < 0:
    print("Sorry, negative numbers can't be armstrong numbers.")

elif num == 0:
    print("Yes, 0 is an armstrong number.")

