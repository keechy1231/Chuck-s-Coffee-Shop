#Ask your customer what their name is with the input() function and store that in the variable NAME.
name = input("What is your name?\n")

#Greet the customer with their name and thank them for coming in today using concatenation.

if name == "Ben":
  answer = input("Are you evil?\n")
  if answer == "yes":
      print("Go away Evil Ben")
      exit()
  else:
        print("Nice, Thank you for coming in not evil " + name)
else:
  print("Hello " + name + ", thank you so much for coming in today.\n\n\n")

  #Coffee menu

menu = "Black Coffee, Espresso, Latte, Cappucino, Frappuccino"

#Ask the customer what they would like from the menu and store it in the variable order.
order = input(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu + "\n")

#Ask the customer how many coffees they would like and store it in the variable QUANTITY
quantity = input("How many coffees would you like?\n")

#Set the price for coffee

if order == "Frappuccino":
  price = 13
elif order == "Black Coffee":
    price = 3
elif order == "Expresso":
    price = 5
elif order == "Latte":
    price = 6
elif order == "Cappucino":
    price = 10
elif order != "Cappucino""Latte":
    print("Sorry we don't serve that here")
    price = 0

#ask if they want wipped cream
whipped_cream = input ("Do you want wipped cream with that?\n")

if whipped_cream == "yes":
    extra = input ("do you want extra whipped cream?\n")
    if extra == "yes":
        print("okay, you can have double the whipped cream")



# print total cost of the order
print("Your total for today is ")
print(int(price)*int(quantity))