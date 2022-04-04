import time

print("Hello, Welcome to Chucks Coffee Shop")
time.sleep(2)
#Ask your customer what their name is with the input() function and store that in the variable NAME.
name = input("What is your name?\n").lower()

#Greet the customer with their name and thank them for coming in today using concatenation.

if name == "ben":
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
order = input(name + ", what would you like from our menu today? Here is what we are serving.\n" + menu + "\n").lower()

#Ask the customer how many coffees they would like and store it in the variable QUANTITY
quantity = input("How many coffees would you like?\n")


price = 0
more = "yes"

#Set the price for coffee
while more == "yes":
    if order == "frappuccino":
        price = price + (13*int(quantity))
    elif order == "black coffee":
        price = price + (3*int(quantity))
    elif order == "expresso":
        price = price + (6*int(quantity))
    elif order == "latte":
        price = price + (7*int(quantity))
    elif order == "cappucino":
        price = price +(10*int(quantity))
    elif order != "black coffee" or "frappuccino" or "expresso" or "latte" or "cappucino":
        print("Sorry we dont server that here")
        more = input("Did you want anything from our menu" + menu ("?"))
    more = input("Do you want anything else with your order?\n")
    if more == "yes":
        input("okay, what else would you like?\n").lower()
        quantity = input("How many of these would you like?\n").lower()
    


#ask if they want wipped cream
#whipped_cream = input ("Do you want wipped cream with that?\n").lower()

#if whipped_cream == "yes":
#    price = price + 2
#    extra = input ("do you want extra whipped cream?\n")
#    if extra == "yes":
#        print("okay, you can have double the whipped cream")
#        price = price + 1

#work out total of the order
total=(int(price)*int(quantity))

# print total cost of the order
print("Your total for today is " + str(price))