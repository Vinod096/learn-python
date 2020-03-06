shares_purchased = 2000

print("Number of shares purchased :",shares_purchased)

amount_paid_per_share = 40.00

print("Amount paid for each share :",amount_paid_per_share)

stockbroker_commission = 3 / 100

print("Commission paid to stockbroker :",stockbroker_commission)

shares_sold = 2000

print("Number of shares sold :",shares_sold)

sold_amount_per_share = 42.75

print("Price of each share when selling :",sold_amount_per_share)

stockbroker_commission = 3 / 100

print("Commission paid to stockbroker for selling shares :", stockbroker_commission)

Amount_paid_for_purchasing_of_shares = shares_purchased * amount_paid_per_share

print("Amount_paid_for_purchasing_of_shares :",Amount_paid_for_purchasing_of_shares)

Commission_while_Purchasing = Amount_paid_for_purchasing_of_shares * stockbroker_commission

print("Commission :",Commission_while_Purchasing)

Sold_stock_amount = sold_amount_per_share * shares_purchased

print("Total amount :",Sold_stock_amount)

Commission_while_Selling = Sold_stock_amount * stockbroker_commission

print("Commission for selling :",Commission_while_Selling)

Total_amount_with_Joe = Sold_stock_amount - Commission_while_Purchasing - Commission_while_Selling

print("Total amount left over with Joe :",Total_amount_with_Joe)