portfolio = [
    ("TCS", "2024-01-10", 3200, 10, 3500),
    ("Infosys", "2024-02-15", 1400, 20, 1350),
    ("Wipro", "2024-03-05", 600, 15, 650)
]

total_cost = 0
total_selling = 0


for share in portfolio:
    _,_, cost_price, quantity, selling_price = share
    total_cost += cost_price * quantity
    total_selling += selling_price * quantity
    
gain_or_loss = total_selling - total_cost

if total_cost != 0:
    percentage = (gain_or_loss / total_cost) * 100
    
else:
    percentage = 0
    
print("Total Cost of Portfolio:", total_cost)
print("Total Amount Gained or Lost:", gain_or_loss)
print("Percentage Profit/Loss: {:.2f}%".format(percentage))