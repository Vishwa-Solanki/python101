
# # #  ctrl + / is how you do comments 

# # # This is a string example
# # print("hello world")
# # print("First day of Python")
# # #  This is number example
# # print(3)
# # print(3+3)

# # learner = "Abc"
# # print(learner)
# # ideal_number_of_pets =3
# # print(ideal_number_of_pets)
# # how_much_of_a_banana = 3.1
# # print(how_much_of_a_banana)

# # is_our_pet_vaccinated = True
# # print(is_our_pet_vaccinated)

# # print(type(how_much_of_a_banana))
# # print(type(is_our_pet_vaccinated))
# # print(type(learner))
# # print(type(ideal_number_of_pets))

# # # Power of example
# # print(3**3)

# # # Modulo
# # print(10%5)
# # print(10%3)

# # # area of ractangle
# # # l x w
# # length = 342
# # width = 20

# # area = length * width
# # print(area)

# # # find text amount 
# # price = 10
# # tax = price * 0.08
# # print(tax)

# # # Find the average
# # avg = (10+10+10)/3
# # print(avg)

# # Input Function
# # length1= float(input("Enter Length: "))
# # width1 = 20
# # area1= length1 * width1
# # print(area1)

# # fav_color = input("Your Favourite coloir is?")

# # print(f"Your Favoriye Color Is {fav_color}")

# #Create a Receipt
# # customer name
# # print("Reciept")
# # print("-------------------------------")
# # customerName = "Vishwa"  
# # print(f"Customer Name: {customerName}")
# # # what they purchased
# # itemPrice = 7.95
# # print(f"Item Price: {itemPrice}")
# # # quantity they purchased
# # quantity = 42
# # print(f"Quantity of Item: {quantity}")
# # # Total cost
# # totalCost = round(itemPrice * quantity, 2)
# # # another way to round
# # roundCost = round(totalCost, 2)
# # print(f"Total Cost: {totalCost}")
# # print(f"Total Cost: {roundCost}")


# #Create a Receipt Using Input
# # customer name
# print("Reciept")
# print("-------------------------------")
# customerName = input("enter customer name: ")  
# print(f"Customer Name: {customerName}")
# # what they purchased
# itemPrice = float(input("enter item price: "))
# print(f"Item Price: {itemPrice}")
# # quantity they purchased
# quantity = int(input("enter quantity: "))  
# print(f"Quantity of Item: {quantity}")
# # Total cost
# totalCost = round(itemPrice * quantity, 2)
# # another way to round
# roundCost = round(totalCost, 2)
# print(f"Total Cost: {totalCost}")
# print(f"Total Cost: {roundCost}")


# # Adding this to Github
# print("Now we have created a Git repo and then adding this additional line of command to try git push and add this to git")

# # Adding this to Github
# print("Now I changed my repo name over github.com then adding this additional line of command to try git push and add this to git and check if new repo is updated or not")

# DAY 2: ----------------------------------------------------------------------------------------------------------

# # Revision String Data types and Data Structure in Python

# randomString = "We dont live here anymore"
# string1= "Hellow world!"
# print(string1)
# print(string1[6])
# print(string1[2:8])
# print(string1[3:])
# print(string1*2)
# print(string1+'Everyone!')
# print(string1.lower())
# print(string1.replace('l','s'))
# print(len(string1))
# print(string1.strip())
# print(string1.split(' '))
# string2=40000
# print(type(string2))
# print(type(str(string2)))

#initializing and declaring variable and value
# floatNumberOne=11.10
# floatNumberTwo = 2/5
# print(floatNumberOne)
# print(floatNumberTwo)
# # checking data type
# print(type(floatNumberOne))
# print(type(floatNumberTwo))
# # Converting float to String
# MyStringOne = str(floatNumberOne)
# MyStringTwo = str(floatNumberTwo)
# print("Floating point into String: ", MyStringOne)
# print("Floating point into String: ", MyStringTwo)
# # checking data type
# print(type(MyStringOne))
# print(type(MyStringTwo))

# Python "List" examples
# mylist=[] # create a empty list
# print(mylist)
# # Create a list of strings.
# string_list = ["Hello", "Python", "World"]
# print(string_list[0])
# # Create a list of numbers.
# number_list = [3, 4, 5, 6, 8, 10]
# print(number_list)
# # Create a list of boolean values.
# boolean_list = [True, False, False, True]
# print(boolean_list)
# # Create a mixed list or list with heterogeneous data
# mixed_list = [3, 4, "Python", True]
# print(mixed_list)

# # Converting String to List
# # Create a string.
# my_string = "Hello World"
# # Create a list of characters from my_string.
# character_list = list(my_string)
# print(character_list)
# # Create a list of substrings from my_string.
# substring_list = my_string.split()
# # Print the results.
# print(my_string)        # Output: "Hello World"
# print(character_list)   # Output: ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
# print(substring_list)   # Output: ['Hello', 'World']
# substring_list[1]= "Y'all"
# print(substring_list)


# # Modifying or Updating a List Element
# my_list = [1, "Hello Python", 7.98]
# # Output: 'Hello Python'
# print("before: ", my_list[1])
# # Output: 'Hello JavaScript'
# my_list[1] = "Hello JavaScript"
# print("after: ", my_list[1])
# # Inser Function
# my_list = [1, 2, 3, 4, 5]
# print(my_list)
# my_list.insert(3,3)
# print(my_list)
# my_list.insert(1,67)
# print(my_list)
# # Append function 
# my_list.append(1)
# my_list.append(2)
# my_list.append(3)
# print(my_list)

# # Concatinating two list:
# # Create two lists.
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# # Add elements to the list using append().
# new_list = list1 + list2
# # Print the new list.
# print(new_list)    # output: [1, 2, 3, 4, 5, 6]

# # Traversing List : FOR Loop
# # Create a list.
# my_list = [1, 2, 3, 4, 5]
# # Traverse the list with a for loop.
# for element in my_list:
#     print(element)
# #  Or use "i" instead of "element"
# for element in my_list:
#     print(element)
# # Traverse the list by accessing the
# # indexes with the range() and len() functions.
# for i in range(len(my_list)):
#     print(f"Index {i} contains: {my_list[i]}")


# # Nested Lists / Two-Dimensional Lists
# # Create a two-dimensional list with three sublists.
# # Each sublist contains three elements.
# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # Print the middle element of the 2D list.
# # Remember that list indexes start at 0.
# print(my_list[1][1])  # output: 5
# print(my_list[0][1]) 
# print(my_list[2][2]) 
# print(my_list[1][1]) 
# print(my_list[1]) # output: [4,5,6]



# # Create a two-dimensional list with three sublists.
# # Each sublist contains three elements.
# my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# # Iterate through each sublist.
# for sublist in my_list:
#     # Iterate through each sublist element.
#     for element in sublist:
#         print(element)
# # output (each on a new line): 1 2 3 4 5 6 7 8 9

# another example 
my_list1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(my_list1[0][1], my_list1[1][2])

# # This targets outer list and the inner list numbers
# for eachnumber in my_list1:
#     print(eachnumber)
#     for number in eachnumber:
#         print(number)

# # OR for different output : only all inner list numbers
# for eachnumber in my_list1:
#     for number in eachnumber:
#         print(number)

# # OR for different output : Only all outer list numbers
# for eachnumber in my_list1:
#     print(eachnumber)

# Nums: -----------
nums=[[1, 2, 3, [4, 5, 6 [7, 8, 9]]],10]
print(nums[0])
print(nums[3][3][3])




