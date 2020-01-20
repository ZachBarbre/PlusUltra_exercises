menu = {
    "Brunch" : {
        "Steak and Eggs": 16.99,
        "Three Egg Breakfast": 8.99,
        "Egg Benedict": 11.99,
        "Biscuit and Gravy": 7.99,
        "Chicken Fingers": 10.99,
        "Chicken Wrap": 8.99,
        "Steak Salad" : 1.99
    },
    "Drinks": {
      "Soft Drink": 1.99,
      "Coffee": 1.99,
      "Orange Juice": 0.99,
      "Milk": 0.55,
      "Water": 0.00
    }
}

menu["Brunch"]["Steak Salad"] = 15.99
menu["Specials"] = {"Soup of the Day" : 8.99, "Catch of the Day": 14.99, "Chef Special": 15.99}
menu["Brunch"]["Three Egg Breakfast"] = {"With Bacon": 9.99, "Without Bacon": 8.99}


tables = [['Egg Benedict', 'Coffee', 'Biscuit and Gravy', 'Coffee', 'Steak and Eggs', 'Soft Drink'], 
['Steak and Eggs', 'Soft Drink', 'Soup of the Day', 'Chicken Wrap', 'Water', 'Chicken Fingers', 'Soft Drink', 'Chef Special']]
# get table input
while True:
    table_number = input("Print which table's receipt? Or press enter for a list of tables. ")
    if table_number.isdigit():
        table_number = int(table_number)
        break
    else:
        for i in range(0, len(tables)):
            print(i, '=', tables[i])


# seperate the food and drink into seperate list and then combine into a list with the food on top and drinks on bottom
foods = []
drinks = []
for item in tables[table_number]:
    if item in menu["Brunch"] or item in menu["Specials"]:
        foods.append(item)
    elif item in menu["Drinks"]:
        drinks.append(item)
    else:
        print("Fix the order!")
order = foods + drinks
# print the item and the cost of the item and calculate the whitespace to keep justified alignment on the $ sign
# add up the cost of the items
items_cost = 0
print('\n')
for item in order:
    whitespace = 30 - len(item) 
    if item in menu["Brunch"]:
        cost_whitespace = 7 - len(str(menu["Brunch"][item]))
        print(item + ' '*whitespace + '$' + ' '*cost_whitespace + str(menu["Brunch"][item]))
        items_cost += menu["Brunch"][item]
    elif item in menu["Specials"]:
        cost_whitespace = 7 - len(str(menu["Specials"][item]))
        print(item + ' '*whitespace + '$' + ' '*cost_whitespace + str(menu["Specials"][item]))
        items_cost += menu["Specials"][item]
    elif item in menu["Drinks"]:
        cost_whitespace = 7 - len(str(menu["Drinks"][item]))
        print(item + ' '*whitespace + '$' + ' '*cost_whitespace + str(menu["Drinks"][item]))
        items_cost += menu["Drinks"][item]
    else:
        print("Something broke. This should not display")
# calculate and print the subtotal, tax and total aligned on the $ sign
items_cost = round(items_cost,2)
cost_whitespace = 7 - len(str(items_cost))
print("\n" + ' '*24 + 'Price: $' + ' '*cost_whitespace + str(items_cost))
tax_cost = round(items_cost * 0.07, 2)
cost_whitespace = 7 - len(str(tax_cost))
print(' '*24 + 'Taxes: $' + ' '*cost_whitespace + str(tax_cost))
total_cost = round(items_cost + tax_cost,2)
cost_whitespace = 7 - len(str(total_cost))
print(' '*24 + 'Total: $' + ' '*cost_whitespace + str(total_cost))


# calculate the suggested tips and print aligned on the $ sign 
tip_high = round(total_cost * 0.25, 2) 
tip_normal = round(total_cost * 0.2, 2)
tip_low = round(total_cost *0.15, 2)
print(' **Suggested Tip**')
cost_whitespace =  11 - len(str(tip_high))
print("Tip 25%:" + ' '*cost_whitespace + '$' + str(tip_high))
cost_whitespace =  11 - len(str(tip_normal))
print("Tip 20%:" + ' '*cost_whitespace + '$' + str(tip_normal))
cost_whitespace =  11 - len(str(tip_low))
print("Tip 15%:" + ' '*cost_whitespace + '$' + str(tip_low) + '\n')






