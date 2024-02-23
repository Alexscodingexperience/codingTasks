# The four items on the menu

menu = {
    "item": "Espresso",
    "item": "Coffee with milk",
    "item": "Latte",
    "item": "Cappuccino",
    }

# The total stock amount of each item

stock_total = {
  "Espresso": 23,
  "Coffee with milk": 11,
  "Latte": 15,
  "Cappucino": 17,
}

# How much each item costs

price_total = {
  "Espresso": 1.00,
  "Coffee with milk": 1.75,
  "Latte": 2.50,
  "Cappucino": 3.00,
}

# Calculating the total value of all the stock

total_stock = 0

for item in stock_total: 
    stock = stock_total[item]
    price = price_total[item]
    total_stock += stock * price

print (f"Total stock is: ${total_stock:.2f}")

