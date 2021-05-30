admin_id="Admin"
admin_password=1234
customer_id="Customer"
customer_password=2345
available_pizzas = ['margarita', 'pollo', '4cheese', 'bolognese', 'vegetarian']
available=[12,6,3,5,4]
available_toppings = ['mushroom', 'onions', 'green pepper', 'extra cheese']
pizza_prices = {'margarita': 500, 'pollo': 700, '4cheese': 600, 'bolognese': 800, 'vegetarian': 650}
topping_prices = {'mushroom':60, 'onions': 80, 'green pepper':70, 'extra cheese':90}
sub_total = []
final_order = {}
customer_adress = {}
while(True):
    choice=int(input("\n\t\t\tpress 1 for admin panel\n\t\t\tpress 2 for customer panel\n\t\t\t press 3 to quit\n\t\t\t"))
    if choice==1:
        #login
        while(True):
            admin_id_input=input('\n\t\t\tenter admin id\n\t\t\t')
            admin_password_input=int(input('\n\t\t\tenter passward\n\t\t\t'))
            if admin_id==admin_id_input and admin_password==admin_password_input:
                print('\n\t\t\tlogin successful\n')
                while(True):
                    admin_choice=input("\n\t\t\tfor managing the stock type'manage' \n\t\t\t to view the stock type 'view' \n\t\t\t to logout type 'logout'\n\t\t\t")
                    if admin_choice=="manage":
                        #stock
                        stock_manage=input("\n\t\t\twould you like to add  or remove stocks\n\t\t\t")
                        while(True):
                            if stock_manage=="add":
                                for pizzas in available_pizzas:
                                    print("\n\t\t\t",pizzas,"=",available[available_pizzas.index(pizzas)])
                                pizza=input("\n\t\t\twhich pizza would you like to add?\n\t\t\t")
                                if pizza in available_pizzas:
                                    add_pizza=int(input("\n\t\t\thow many pizza will you like to add?\n\t\t\t"))
                                    
                                    available[available_pizzas.index(pizza)]=int(available[available_pizzas.index(pizza)])+add_pizza
                                    print("\n\t\t\ttotal",pizzas,"pizza is",available[available_pizzas.index(pizza)],"\n")
                                    break
                                else:
                                    print("\n\t\t\twrong choice\n")
                            elif stock_manage=="remove":
                                for pizzas in available_pizzas:
                                    print("\n\t\t\t",pizzas,"=",available[available_pizzas.index(pizzas)])
                                pizza=input("\n\t\t\twhich pizza would you like to remove?\n\t\t\t")
                                if pizza in available_pizzas:
                                    remove_pizza=int(input("\n\t\t\thow many pizza will you like to remove?\n\t\t\t"))
                                    if remove_pizza>available[available_pizzas.index(pizza)]:
                                        print('\n\t\t\tsorry we only have',available[available_pizzas.index(pizza)],'pizza available\n')
                                    else :
                                        available[available_pizzas.index(pizza)]=int(available[available_pizzas.index(pizza)])-remove_pizza
                                        print("\n\t\t\ttotal",pizzas,"pizza is",available[available_pizzas.index(pizza)])
                                        break
                                else:
                                    print("\n\t\t\twrong choice\n")
                    elif admin_choice=="view":
                        #view_stock
                        for x in range(0,5):
                            print("\n\t\t\t",available_pizzas[x]," pizza=",available[x])
                        print()
                    elif admin_choice=="logout":
                        print("\n\t\t\tthank you for coming\n")
                        break
                    else:
                                print("\n\t\t\twrong choice\n")
            if admin_choice=="logout":
                break        
                  
            else:
                print('\n\t\t\tinvalid id passward\n')
                break
        
        
    elif choice==2:
        
        #login
        while(True):
            customer_id_input=input('\n\t\t\tenter customer id\n\t\t\t')
            customer_password_input=int(input('\n\t\t\tenter passward\n\t\t\t'))
            if customer_id==customer_id_input and customer_password==customer_password_input:
                print('\n\t\t\tlogin successful\n')
                
                #ordering a pizza
                print("\n\t\t\tHi, welcome to our text based pizza ordering\n")
                order_pizza = True
                while order_pizza:    
                    print("\n\t\t\tPlease choose a pizza: ")
                    
                    for pizzas in available_pizzas:
                        print("\n\t\t\t",pizzas,"\n")
                        
                    while True:
                        pizza = input("\n\t\t\twhich pizza would you like to order?\n\t\t\t")
                        if pizza in available_pizzas:
                            if available[available_pizzas.index(pizza)]>0:
                                print(f"\n\t\t\tYou have ordered a {pizza}.\n")
                                available[available_pizzas.index(pizza)]-=1
                                sub_total.append(pizza_prices[pizza])
                                break
                            else:
                                print("\n\t\t\tout of stock")
                        if pizza not in available_pizzas:
                            print(f"\n\t\t\tI am sorry, we currently do not have {pizza}.\n")

                    #asking for extra toppings
                    order_topping = True
                    print("\n\t\t\tThis is the list of available extra toppings: \n")
                    for toppings in available_toppings:
                        print("\n\t\t\t",toppings,"\n")
                        
                    while order_topping:
                        extra_topping = input("\n\t\t\tWould you like an extra topping? yes or no?\n\t\t\t")
                        if extra_topping == "yes":
                            topping = input("\n\t\t\tWhich one would you like to add?\n\t\t\t")
                            if topping in available_toppings:
                                final_order.setdefault(pizza, [])
                                final_order[pizza].append(topping)
                                print(f"\n\t\t\tI have added {topping}.\n")
                                sub_total.append(topping_prices[topping])
                            else:
                                print(f"\n\t\t\tI am sorry, we don't have {topping} available\n.")

                        elif extra_topping == "no":
                            break
                    extra_pizza = input("\n\t\t\tWould you like to order another pizza?\n\t\t\t")
                    if extra_pizza == "no":
                        for key, value in final_order.items():
                            print(f"\n\t\t\tYou have order a {key} pizza with {value}")
                        check_order = True
                        while check_order:
                            
                            order_correct = input("\n\t\t\tIs this correct? yes/no \n\t\t\t")
                            if order_correct == "yes":
                                check_order = False
                                order_pizza = False
                            if order_correct == "no":
                                print(final_order)
                                add_remove = input("\n\t\t\twould you like to add or remove? \n\t\t\t")
                                if add_remove == "remove":
                                    remove = input("\n\t\t\tWhich pizza would you like to remove? \n\t\t\t")
                                    del final_order[remove]
                                    print(final_order)
                                if add_remove == "add":
                                    check_order = False

                #finalizing the order
                print(f"\n\t\t\tYour total order price is: Rs{sum(sub_total)}")

                print("\n\t\t\tPlease provide us with your name, adress and phonenumber")
                customer_adress['name'] = input("\n\t\t\twhat is your name?\n\t\t\t")
                customer_adress['street_name'] = input("\n\t\t\tWhat is your streetname and housenumber?\n\t\t\t")
                customer_adress['postalcode'] = input("\n\t\t\tWhat is the postalcode and cityname?\n\t\t\t")
                customer_adress['phonenumber'] = input("\n\t\t\tWhat is your phonenumber?\n\t\t\t")
                
                print(f"\n\t\t\tThank you for your order {customer_adress['name']}.\n")
                
                print("\n\t\t\tWe will deliver your order to this adres ASAP\n")
                
                print(customer_adress['\n\t\t\tstreet_name'])
                print(customer_adress['\n\t\t\tpostalcode\n'])
                
                print(f"\n\t\t\twe will contact you on {customer_adress['phonenumber']} if anything comes up.")
                break
            else:
                print('\n\t\t\tinvalid id passward')
    else:
        print("\n\t\t\tthank you for using the app")
        break

