def delivery_price(order_size=None, is_member=None):
    if order_size is None:
        try:
            order_size = float(input("Hvor meget skal din bestilling være?: "))
        except ValueError:
            return "Der skete en fejl, vil du prøve igen?"
    
    if is_member is None:
        member_input = input("Er du medlem? (ja/nej): ").strip().lower()
        if member_input == "ja":
            is_member = True
        elif member_input == "nej":
            is_member = False
        else:
            return "Ugyldigt input, prøv venligst igen."

    if order_size < 100:
        return "Bestillingsstørrelsen skal være mindst 100."
    elif is_member:
        return 0.0
    elif order_size <= 300:
        return 40.0
    else:
        return 0.0

