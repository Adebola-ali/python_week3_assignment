def calculate_discount(price, discount_percent):
    if discount_percent >= 0.2:
        # discount = discount_percent * price
        final_price = price - discount
        return final_price 
    else:
        final_price = price
        return final_price   
        
# taking user input
price  = int(input("Enter original price: "))    
discount_percent  = float(input("Enter discount percentage: "))
discount = discount_percent * price
print(f'You are given {discount} discount\n Your payment is: {calculate_discount(price, discount_percent)}')    



