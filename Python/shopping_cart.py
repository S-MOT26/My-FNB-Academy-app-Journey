
#Create a shopping cart that will continuasly ask the user for a food product and the price of that product
#Have an exit clause if the user wishes to stop adding more things to their cart
#At the end show the food items and the total cost to the user

foods = []
prices = []

while True:
    food = input("Enter a food to buy or press 'q' to quit: ")
    if food.lower() == 'q':
        break
    try:
        price = float(input(f"Enter the price of {food}: R"))
    except ValueError:
        print("Please enter a valid price.")
        continue

    foods.append(food)
    prices.append(price)

# Show the final cart
print("\n ----- YOUR CART -----")
total = 0
for food, price in zip(foods, prices):
    print(f"{food} - R{price:.2f}")
    total += price

print(f"\n Your total is: R{total:.2f}")