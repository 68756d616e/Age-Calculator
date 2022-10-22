# Age calculator
# If you were to live until 100, how long will you have remaining from your current age?

#Input your current age
age = input("What is your current age?")

a = 100 - int(age)
days = (a) * 365
months = (a) * 12
weeks = (a) * 52

print(f"You have {days}, {weeks} weeks, and {months} months remaining")

#Alternative

#age = input("Please enter your age: ")

#age_int = 100 - int(age)
#years = age_int * 365
#months = age_int * 12
#weeks = age_int * 52

#print(f"You have {years}, {months} months, and {weeks} weeks left")





