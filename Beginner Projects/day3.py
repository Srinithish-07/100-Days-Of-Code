# DAY 3
# Topics Learned

    # Conditional Statements ---> if , if/else , if/elif/else
    # Comparison Operators --->  > , < , >= , <= , == , !=
    # Logical Operators ---> and , or , not
    # Code Blocks and Scope

# Leap Year Program...
# year = int(input("Enter a year to check : "))
# if year % 4 ==0:
#     if year % 100 == 0:
#         if year % 400 == 0:
#             print(f"{year} is a leap year")
#         else:
#             print(f"{year} is not a leap year")
#     else:
#         print(f"{year} is a leap year")
# else:
#     print(f"{year} is not a leap year")


### Pizza Order Practice

# print("Welcome to the PIZZA PARADISE.....\n")
# print("Price details...")
# print("""Small pizza (S): $15
# Medium pizza (M): $20
# Large pizza (L): $25
      
# Add pepperoni for small pizza : +$2
# Add pepperoni for medium or large pizza : +$3
# Add extra cheese for any size pizza : +$1\n""")

# size = input("What size pizza do you want? S, M, or L : ").upper()
# add_pepperoni = input("Do you want pepperoni? Y or N : ").upper()
# extra_cheese = input("Do you want extra cheese? Y or N : ").upper()

# bill = 0

# if size == 'S':
#     bill += 15
# elif size == "M":
#     bill += 20
# else:
#     bill += 25

# if add_pepperoni == 'Y':
#     if size == 'S':
#         bill += 2
#     else:
#         bill += 3

# if extra_cheese == 'Y':
#     bill += 1
            
# print("Thank you for choosing Pizza Paradise...")
# print(f"Your total bill is : ${bill}")
# print("Enjoy your meal...")


##### TREASURE ISLAND...

# For a more complex game with multiple stages or additional logic: Version 2 provides better control and flexibility.

# print('''
# *******************************************************************************
#           |                   |                  |                     |
#  _________|________________.=""_;=.______________|_____________________|_______
# |                   |  ,-"_,=""     `"=.|                  |
# |___________________|__"=._o`"-._        `"=.______________|___________________
#           |                `"=._o`"=._      _`"=._                     |
#  _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
# |                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
# |___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
#           |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
#  _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
# |                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
# |___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
# ____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
# /______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
# ____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
# /______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
# ____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
# /______/______/______/______/______/______/______/______/______/______/_____ /
# *******************************************************************************
# ''')
# print("Welcome to Treasure Island.")
# print("Your mission is to find the treasure.")
# continue_game = True

# choice_1 = input('You\'re at a cross road. Where do you want to go? Type "right" or "left": ').lower() 

# if choice_1 == "right":
#     print("You fell into a hole. Game Over.")
#     continue_game = False

# if continue_game:
#     print("\nYou've come to a lake. There is an island in the middle of the lake.")
#     choice_2 = input('Type "wait" to wait for a boat. Type "swim" to swim across: ').lower()

#     if choice_2 == "swim":
#         print("\nYou decided to swim across the lake and got eaten by a sea monster. Game Over.")
#         continue_game = False

#     elif choice_2 == "wait" and continue_game:
#         print("\nYou waited for a boat and crossed the lake safely.")
#         print('You arrived at the island unharmed. There is a house with 3 doors.One red, one yellow, and one blue.')
#         choice_3 = input("Which colour do you choose?: ").lower()
#         print()

#         if choice_3 == "red":
#             print("It's a room full of fire. Game Over.")
        
#         elif choice_3 == "yellow":
#             print("You found the treasure! You Win!")
        
#         elif choice_3 == "blue":
#             print("You enter a room of beasts. Game Over.")
#         else:
#             print("Invalid choice. Game Over.")



# optimised code

# For a simple, straightforward game with few stages: Version 1 is more readable and easier to manage.

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice_1 = input('You\'re at a cross road. Where do you want to go? Type "right" or "left": ').lower()

if choice_1 == "left":
    choice_2 = input('''\nYou've come to a lake. There is an island in the middle of the lake.
Type "wait" to wait for a boat. Type "swim" to swim across: ''')
    if choice_2 == "wait":
        choice_3 = input('''\nYou arrived at the island unharmed. There is a house with 3 doors.One red, one yellow, and one blue.
Which colour do you choose?: ''').lower()
        print()
        if choice_3 == "red":
            print("It's a room full of fire. Game Over.")
        elif choice_3 == "yellow":
            print("You found the treasure! You Win!")
        elif choice_3 == "blue":
            print("You enter a room of beasts. Game Over.")
        else:
            print("Invalid choice. Game Over.")
    else:
        print("\nYou decided to swim across the lake and got eaten by a sea monster. Game Over.")
else:
    print("You fell into a hole. Game Over.")
