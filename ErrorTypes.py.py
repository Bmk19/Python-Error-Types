# This example program is meant to demonstrate errors.

print("Welcome to the error program")
print("\n")

ageStr = "24 years old"
#Fixed a compilation error to remove an unnecessary indentation before ageStr

age = int(24)
#Fixed a run-time error where 24 was not specified as an integer


print("I'm "+str(age)+" years old.")
three = int(3)

#Fixed a logical error where the printed age was not 27.
answerYears = age + three

print("The total number of years:" + str(answerYears))
#Fixed a syntax error where brackets () were not surrounding the total no. of years
answerMonths = answerYears*12
print("In 3 years and 6 months, I'll be " + str(answerMonths + 6) + " months old")

#HINT, 330 months is the correct answer

