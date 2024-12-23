#Objective: make a project
#
#
# 
# 
# 
def total_price(quantity, price):
    return quantity * price

def final_price(discounted_price):
    return round((discounted_price + tax_onit(discounted_price)), 2)

def tax_onit(discounted_price):
    TAX_RATE = 8.5
    return round((TAX_RATE * discounted_price / 100), 2)

def discounted_price(tot_price):
    if tot_price > 500:
        discount = 20
    elif tot_price  >200:
        discount = 15
    elif tot_price >100:
        discount = 10
    elif tot_price >50:
        discount = 5
    else:
        discount = 0
    return tot_price - (discount*tot_price/100)

def display_items(girls_shampoo,boys_shampoo,cows_shampoo):
    print("\n SHAMPOO MARKET PLACE")
    print("___________________________________________\n")
    print(" Enter '0' to check out: ")
    print(" code:1 product name:girls shampoo: 35.65$ : In stock ", girls_shampoo, end="")
    print(" code:2 product name:boys shampoo : 29.33$ : In stock ", boys_shampoo)
    print(" code:3 product name:cows shampoo : 1.99$ : In stock ", cows_shampoo)
    print("\n")

def input1():
    tota = 0
    girls_shampoo = 4
    boys_shampoo = 2
    cows_shampoo = 9
    while True:
        display_items(girls_shampoo,boys_shampoo,cows_shampoo)
        try:
            a = int(input("enter product code: "))
        except:
            print("value input error")
        if a == 0:
            print("You have left shampoo market")
            break
        elif a == 1:
            b = int(input("how many girls shampoo do you want: "))
            price = 35.65
            
            if b <= girls_shampoo:
                girls_shampoo =girls_shampoo- b
                tota += total_price(b, price)
            else:
                print("Not enough stock available!")
                
        elif a == 2:
            b = int(input("how many boys shampoo do you want: "))
            price = 29.33
            if b <= boys_shampoo:
                boys_shampoo = boys_shampoo-b
                tota += total_price(b, price)
            else:
                print("Not enough stock available!")
        elif a == 3:
            try:
                b = int(input("how many cows shampoo do you want: "))
            except:
                print("value input error")
            price = 1.99
            if b <= cows_shampoo:
                cows_shampoo =cows_shampoo- b
                tota += total_price(b, price)
            else:
                print("Not enough stock available!")
        else:
            print("product doesnt exist")
    print(final_price((discounted_price(tota))))
input1()