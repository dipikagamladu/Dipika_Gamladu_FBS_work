#write a program to calculate selling price of book based on cost price and discount.
cost_price = int(input('Enter cost price:'))
discount = int(input('Enter discount percentage:'))
discount_amount = cost_price * discount/100
selling_price = cost_price-discount
print('selling_price of book=',selling_price)