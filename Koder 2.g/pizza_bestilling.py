def delivery_price(order_size = None, is_member = None):
    if order_size is None:
        order_size = float(input("Hvor meget skal det være din bestilling?: "))
        
    if is_member is None:
        member_input = input("Er du medlem?: ").strip().lower()
        if member_input == "ja":
            is_member = True
        elif member_input == "nej":
            is_member = False
        else:
            return 0.0
    
    if order_size < 100:
        return "Bestilling skal være mindst 100"
    elif is_member:
        return 0.0
    elif order_size <= 300:
        return 40.0
    else:
        return 0.0
    
def order_summary():

print(delivery_price())
