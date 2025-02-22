# DAY 2

# Topics Learned

    # Data Types ---> String -> "Hello" , Integer -> 717 , Float -> 3.141598 , Boolean -> True || False

    # Mathematical Operations ---> 7+1 , 8-2 , 2*6 , 6/3 , 2**3(order) , 7//3(floor div) , uses BOD MAS

    # compound or augmented assignment operators ---> +=, -=, *=, /=
     
    # BOD MAS --> ()[brackets] , **[orders] , /*[div and mul] , +-[add and sub]

    # Type Conversions ---> type() function [gives datatype of variable] int to float,str and vice versa

    # f - Strings --> is a way to embed expressions inside string literals, using curly braces {}
                    # types of formating strings
                    # f strings -> Format = f"Hello, my name is {name} and I am {age} years old."
                    # % operator -> Format = "Hello, my name is %s, and I am %d years old." % (name, age)
                    # format() -> Format = "Hello, my name is {} and I am {} years old.".format(name, age)  

    # Number manipulation --> round() function --> round(2.666666,2) --> 2.67 
    # [it rounds off and gives 2 nums after decimal]

    # subscript --> print("Hello"[0]) gives H , which prints the letter at 0th index (only works for strings)

    # In Python, the underscore (_) can be used as a digit separator in numeric literals to improve readability.
    # This feature was introduced in Python 3.6 (PEP 515). The underscores do not affect the value of the number
    # they are simply ignored by the compiler.

    # Therefore, 123,456,789 and 123_456_789 are treated as the same value by the Python compiler.


##### TIP CALCULATOR AND BILL SPLIT FOR EACH...


print()
# Create a greeting for your program.
print("Welcome to Tip Calculator...")

#Ask for the total bill.
bill = float(input("What is the Total Bill : $"))

#Ask for the tip percentage.
tip_percentage = float(input("How much tip would you like to give? like 10 , 12 or 15% of bill? : "))

# Ask for the no. of persons to split.
no_of_persons = int(input("How many people to split the bill? : $")) 

# calculated by adding the bill with tips and dividing according to the split
# share per person = ((bill + ((tip_percentage/100)*bill))/split) optimised code 

#calcutale the tip amount
total_tip = bill * (tip_percentage)/100

# add the tip with the total bill and divide it with the no_of_persons to get the share for each person
final_bill = bill + total_tip
share_per_person = round(final_bill / no_of_persons,2) # round doesn't work properly for float points
share_per_person = "{:0.2f}".format(final_bill / no_of_persons)

# print the share of each person
print(f"Each person should pay : ${share_per_person}")

