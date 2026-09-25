

def calculate_order_total(order_total: float, is_member: bool, has_coupon: bool) -> float:

    if order_total < 50:

        discount = 0.0
    elif is_member:
        
        if order_total > 200:
            discount = 0.20
        
        else:
            discount = 0.10
    elif has_coupon:
      if order_total>100:
        discount = 0.05
      else:
        discount = 0.00
    else:
       discount=0.0     
    calculated_order_total = order_total * (1 - discount)
    return round(calculated_order_total, 2)















