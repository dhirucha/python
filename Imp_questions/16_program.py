 #Dictionary of grocery items with their prices
prices = {
    'Rice': 50,
    'Wheat': 40,
    'Sugar': 45,
    'Oil': 120
}

# Dictionary of grocery items with quantity purchased
quantities = {
    'Rice': 2,      # 2 kg
    'Wheat': 3,     # 3 kg
    'Sugar': 1,     # 1 kg
    'Oil': 1        # 1 liter
}

total_bill = 0
for item in prices:
    item_total = prices[item] * quantities.get(item,0)
    print(f"{item} : {prices[item]} X {quantities[item]} = {item_total}")
    
    total_bill += item_total
    
    print("Total bill is: ", total_bill)