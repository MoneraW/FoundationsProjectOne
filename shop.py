####################### DO NOT MODIFY THIS CODE ########################
menu = {
    "original cupcake": 2,
    "signature cupcake": 2.750,
    "coffee": 1,
    "tea": 0.900,
    "bottled water": 0.750
}
original_flavors = ["vanilla", "chocolate", "strawberry", "caramel", "raspberry"]
original_price = 2
signature_price = 2.750

############################# Start Here! ##############################
cupcake_shop_name = "Oh My Cake!"
signature_flavors = ["vanilla","funfetti","fudge"]
order_list = []


def print_menu():
    """
    Print the items in the menu dictionary.
    """
    print("Our menu:")
    # your code goes here!
    for menu_item in menu:
        print(menu_item, menu[menu_item])


def print_originals():
    """
    Print the original flavor cupcakes.
    """
    print("Our original flavor cupcakes (KD %s each):" % original_price)
   
    # your code goes here!
    for original_f in original_flavors:
        print(original_f)
    


def print_signatures():
    """
    Print the signature flavor cupcakes.
    """
    print("Our signature flavor cupcake (KD %s each):" % signature_price)
    
    # your code goes here!
    for s_flavor in signature_flavors:
        print(s_flavor)
    

def is_valid_order(order):
    """
    Check if an order exists in the shop.
    """
    # your code goes here!
    if order in menu or order in original_flavors or order in signature_flavors:
        return True
    else:  
        return False



def get_order():
    """
    Repeatedly ask customer for order until they end their order by typing "Exit".
    """
    order_list = []
    # your code goes here!
    #print
    order = input("what's your order? (Enter the exact spelling of the item, and make sure to type 'exit' when you're done)\n")
    #order = input()

    while order != "exit":
        if is_valid_order(order):
            order_list.append(order)
        order = input()
    #while order in order_list:
    #if order_input == is_valid_order:
     #   order_list.append(order_input)
    #elif: order_input == "exit"
    return order_list


def accept_credit_card(total):
    """
    Return whether an order is eligible for credit card payment.
    """
    # your code goes here!
    if total >= 5:
        return True
    else:
        return False

def get_total_price(order_list):
    """
    Calculate and return total price of the order.
    """
    total = 0
    # your code goes here!
    for order in order_list:
        order = order.lower()
        if order in menu:
            total += menu[order]
        elif order in original_flavors:
            total += original_price
        elif order in signature_flavors:
            total += signature_price


    return total

def print_order(order_list):
    """
    Print the order of the customer.
    """
    print()
    print("Your order is: ")
    # your code goes here!
    for order in order_list:
        print(" %s" % order)

    print()
    price = get_total_price(order_list)
    print("your total is %s KD" % price)
    if accept_credit_card(price):
        print("This order is eligible for credit card payment")

    print("Thank you for shopping at Oh My Cake!")







