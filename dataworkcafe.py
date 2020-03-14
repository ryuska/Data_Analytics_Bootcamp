menu={
    'Coffee':[
        {'Espresso':1.50},
        {'Americano':2.00},
        {'Caffe latte':2.25},
        {'Mocha':2.25},
        {'Cappuccino':2.50},
        {'Macchiato':2.50}
        ]
    ,
    'Tea': [
        {'White tea':1.50},
        {'Green tea':2.00},
        {'Oolong tea':2.25},
        {'Black tea':2.25},
        {'Earl Grey':2.50},
        {'Matcha':2.50}
       ],
       'Pastries': [
           {'Croissant':5.50},
           {'Cinnamon roll':4.50},
           {'Banana bread':4.25},
           {'Pumpkin bread':3.75},
           {'Sticky bun':4.25},
           {'Apple turnover':3.75}
       ]}

def greet_customer():
    print('Welcome to DataWork Cafe!')
    customer_input=input('Would you like to see a menu? (Y/N)\n')
    while (customer_input.upper() != 'Y' and customer_input.upper() != 'N'):
        customer_input = input("Sorry I didn't quite catch that, would you like to see a menu? (Y/N)\n")
    return customer_input

def show_menu(menu):
    for type in menu:
        print(type)
        for items in menu[type]:
            for item in items:
                print('\t',item,'-','$'+str(items[item]))
    return

def check_menu(order_item):
    item_exists=False
    found_item=[]
    for type in menu:
        for items in menu[type]:
            for item in items:
                if item.upper() == order_item.upper():
                    item_exists=True
                    found_item.append({item:items[item]})
    if not item_exists:
        return False
    print(found_item)
    return found_item

def order():
    order_list=[]
    customer_input=input("Would you like to order? (Y/N)\n")
    while (customer_input.upper() != 'Y' and customer_input.upper() != 'N'):
        customer_input=input("Sorry I didn't quite catch that, would you like to order? (Y/N)\n")
    if customer_input !='Y':
        print('Thank you, come again!')
        return order_list
    while customer_input.upper() == 'Y':
        quantity=0
        customer_order = {}
        order_item = input("What item would you like?\n")
        order_det=check_menu(order_item)
        item_key=''
        if order_det:
            for od in order_det[0]:
                item_key = od
            customer_order['price'] = order_det[0][item_key]
            quantity = input('How many of those would you like?\n')
            customer_order['order'] = order_item
            customer_order['quantity'] = quantity
            customer_order['total'] = int(quantity) * customer_order['price']
            order_list.append(customer_order)
        else:
            print('The item you chose is not on our menu.')
        customer_input=input("Would you like to place another order?")
        while customer_input.upper() != 'Y' and customer_input.upper() != 'N':
            customer_input = input("Y OR N dumbass")
    return order_list

def reciept(orderlist):
    print('Reciept')
    before_tax_total=0
    for item in orderlist:
        print(item)
        before_tax_total=before_tax_total+item['total']
    tax_amount=before_tax_total*.06
    grand_total=before_tax_total+tax_amount
    print(' Order Total: ',before_tax_total,'\n','Tax amount: ',tax_amount,'\n','Total: ',grand_total)


customer_input = greet_customer()
if customer_input == 'Y':
    input_2 = show_menu(menu)
    orders = order()
    if orders:
        reciept(orders)