#
# Justin Harsha
# Date 1/13/2025
# Sales Prediction Programming Project
# COSC 1010
#

# Variables to hold the sales total and the profit
projectedSales = 0
netProfit = 0
profitAfterExpenses = 0
textDisplay = f""

# Constant for profit precentage of sales
PRECENT_OF_SALES_PROFIT = 0.23

# Get the amount of projected sales.
projectedSales = input("Projected sales............$")

# Calculate the projected profit.
projectedSales = round(float(projectedSales), 2)
profitAfterExpenses = round(float(projectedSales * PRECENT_OF_SALES_PROFIT), 2)
netProfit = profitAfterExpenses + projectedSales

# Print the projected profit.
textDisplay = f"Net profit.................${netProfit}"
print(textDisplay)
textDisplay = f"Profit after expenses......${profitAfterExpenses}"
print(textDisplay)

