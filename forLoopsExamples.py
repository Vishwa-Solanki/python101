# # If statments
# # and If statement is used to compare things

# variable = input("This is an input that will take a response")
# print(variable)

# #  Example: Going to ride cooney island roller coaster
#             # height restriction is 4' aka 48 inches
# height = 52
# if height >= 48:
#     print("You may ride")
# else:
#     print("You cannot ride")

# # Input example with if
# height1= int(input("How tall are you?: "))
# if height >= 48:
#     print("You may ride")
# else:
#     print("You cannot ride")


# # Example: Create a password checker
# # Username: HotDogWater123
# # Password: bluepen
# password = "bluepen"
# userLoginInput = input("Enter Password: ")
# # one '=' is equivqlent to assigning a value and two '==' used for comparision
# if userLoginInput == password:
#     print("Open Sesame")
# else:
#     print("Access Denied")

# Example: If number is even or odd
# number = 19
# if number%2 == 0:
#     print("Number is Even")
# else:
#     print("Number is Odd")
# # Input with this example
# number = int(input("Enter a number: "))
# if number%2 == 0:
#     print("Number is Even")
# else:
#     print("Number is Odd")
# # If number is even or odd using '!=' sign
# number = int(input("Enter a number: "))
# if number%2 != 0:
#     print("Number is Odd")
# else:
#     print("Number is Even")
# # If number is even or odd using == 1 because any number divide by 2 gives only 0 or 1
# number = int(input("Enter a number: "))
# if number%2 -= 1:
#     print("Number is Odd")
# else:
#     print("Number is Even")

# # For Loop: --------------------------------------------------------------------------------
# # Write a for loop for the value 1-152
# # numbers = [1,2,3,4,...]
# for number in range(1,153):
#     print(number)

# # Countdown from 10-0
# for number in range(10,0,-1):
#     print(number)

# # Example: Who likes rootbeear?
# numberOfRootBeers = int(input("Number of bottles of root beer in fridge"))

# for i in range(numberOfRootBeers,1,-1):
#     print(f"{i}Bottle of rootbeer on the wall...")
#     print(f"{i}Bottle of rootbeer...")
#     print("take on down, pass it around...")
#     print(f"{i-1}Bottle of rootbeer on the wall...")

# # Example: What is the sum of 1-427
# total = 0

# for number in range(1,428):
#     total += number

# print(f"your total is : {total}")

# # Example: #update if statement  to while loop so that users can have multiple attempts
# password = 'Hello'
# userLoginInput = input('Enter password: ') 
# while userLoginInput != password:
#     print('Wrong password - please try again ')
#     userLoginInput = input('Enter password ')
# print('Open Sesamo')

# # Example: Find largest number
# numberList = [7, 42,8, 846, -1, 4235, 6, 730]
# largestNumber = numberList[0]
# print(largestNumber)
# for number in numberList:
#     if number > largestNumber:
#         largestNumber = number
# print(largestNumber)

# # Example: Who wants to play.....Guess That Number!
# secretNumber = 7
# guess = 0

# while guess != secretNumber:
#     guess = int(input("Guess the Secret Number:"))
# print("You Got it")

# Example: Who wants to play.....Guess That Number!
secretNumber = 7
guess = 0

while guess != secretNumber:
    guess = int(input("Guess the Secret Number:"))
print("You Got it")