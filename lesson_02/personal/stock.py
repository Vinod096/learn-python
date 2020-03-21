#12. S tock Transaction Program
#Last month Joe purchased some stock in Acme Software, Inc. Here are the details of the
#purchase:
#• The number of shares that Joe purchased was 2, 000.
#• When Joe purchased the stock, he paid $40.00 per share.
#• Joe paid his stockbroker a commission that amounted to 3 percent of the amount he
#paid for the stock.
#Two weeks later Joe sold the stock. Here are the details of the sale:
#• The number of shares that Joe sold was 2, 000.
#• He sold the stock for $42.75 per share.
#• He paid his stockbroker another commission that amounted to 3 percent of the amount
#he received for the stock.
#Write a program that displays the following information:
#• The amount of money Joe paid for the stock.
#• The amount of commission Joe paid his broker when he bought the stock.
#• The amount that Joe sold the stock for.
#• The amount of commission Joe paid his broker when he sold the stock.
#• Display the amount of money that Joe had left when he sold the stock and paid his
#broker(both times). If this amount is positive, then Joe made a profit. If the amount is
#negative, then Joe lost money.

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

print("Commission paid for purchasing :",Commission_while_Purchasing)

Sold_stock_amount = sold_amount_per_share * shares_purchased

print("Total amount after selling shares :",Sold_stock_amount)

Commission_while_Selling = Sold_stock_amount * stockbroker_commission

print("Commission for selling :",Commission_while_Selling)

Total_amount_with_Joe = (Sold_stock_amount - Commission_while_Selling - Commission_while_Purchasing)

print("Total amount left over with Joe :",Total_amount_with_Joe)
