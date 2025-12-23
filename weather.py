
weather = "cold"

if weather == "sunny":
    print("It is sunny.")
    
else:
    print("It is not sunny.")
    



def addition(num1, num2, num3):
    sum_total = num1 + num2 + num3
    print(sum_total)
    
addition(4, 8, 12)

def product(num1, num2):
    product_total = num1 * num2
    print(product_total)
    
product(6, 18)


def check_weather(weather):
    if weather == "sunny":
        print("It is sunny.")
    
    else:
        print("It is not sunny.")
        
check_weather("cold")


def introduction(first_name, last_name):
    full_name = f"{first_name} {last_name}"
    print(f"Hello my name is {full_name}")
    
introduction("Adam", "Smith")



first_name = "John"
last_name = "Doe"
full_name = f"{first_name} {last_name}"
print(f"Hello my name is {full_name}")


def check_length(first_name):
    if len(first_name) > 5:
        print("Your name is long.")
    else:
        print("Your name is short.")
        
check_length("Daniel")



def check_fav_colour(colour):
    if colour.lower() == "blue":
        print("Blue is a cool colour!")
    else:
        print("Nice choice!")

check_fav_colour("Blue")
check_fav_colour("Red")



def check_number_size(number):
    if number > 10:
        print("Big number!")
    else:
        print("Small number!")

check_number_size(15)
check_number_size(5)





def check_score(score):
    if score >= 50:
        print("You passed the level!")
    else:
        print("Try again!")

check_score(50)
check_score(49)


