#!/usr/local/bin/python3

import colored
import os

print(colored.stylize("\n---- | The Laplace probability | ----\n", colored.fg("red")))

len_of_results = int(input("How many results does your experiment have?\n"))
results = []
print("Enter each possible result: \n")

for i in range(len_of_results):
    results.append(input(""))

# function to calculate probability ...
def probability_function(result=None, quantity=results):
    # ... for one result
    if result in results:
        return 1/len(results)

    # ... for every result in given quantity
    return [1/len(results) for i in quantity]

# Check if all probabilities of each result == 1 (100%)
# def check():
#     x = 0
#     for j in probability_function():
#         x += j
#     if x == 0.9999999999999999:
#         return True
#     else:
#         print(x)
#         return False

print(colored.stylize("\nOptions:", colored.fg("green")))
print(">>> '1' Calculate probability of one result")
print(">>> '2' Calculate probability of a quantity of results")
print(">>> 'q' End program")
user_input = input(": ")

if user_input == "q":
    os.system("clear" if os.name == "posix" else "cls")
    exit()
elif user_input == "1":
    result = input("\nEnter the result you want to calculate the probability for: ")
    if result in results:
        print(f"The probability of {result} is: {round(probability_function(result=result)*100, 3)}%\n")
    else:
        print("Your result is not in the quantity of results!\n")

elif user_input == "2":
    quantity_of_results = [int(i) for i in input("\nEnter the a quantity of results (seperated with commas) you want to calculate the probability for: ").split(", ")]
    probabilities_of_results = probability_function(quantity=quantity_of_results)
    probability_of_quantity = 0
    for i in probabilities_of_results:
        probability_of_quantity += i
    print(f"The probability of {quantity_of_results} is: {round(probability_of_quantity*100, 3)}%\n")

else:
    print("\nUnknown input\n")
    os.system("clear" if os.name == "posix" else "cls")
    exit()
