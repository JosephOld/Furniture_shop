def print_catalog(catalog):
    number = 1
    for key, value in catalog.items():
        print(f"{number}. {key}: {value}")
        number = number + 1


def print_basket(basket):
    if check_is_empty(basket) == False:
        number = 1
        for i in basket:
            print(f"{number}. {i}")
            number = number + 1
    else:
        print("Empty basket")


def check_catalog_product(catalog, product):
    result = False
    for i in catalog:
        if i == product:
            result = True
            break
    return result


def print_price(catalog):
    product = input("name the product:  ")
    if check_catalog_product(catalog, product) == True:
        print(f"{product}: {catalog[product]}")
    else:
        print("Product is out of stock")


def addition(catalog, basket,sum):
    product = input("name the product yuo want to add :  ")
    if check_catalog_product(catalog,product) == True:
        basket.append(product)
        sum = sum + catalog[product]
        print(f"{product} was added")

    else:
        print(f"{product} is not available")
    return sum

def check_products(basket, bad_product):
    available_in_list = False
    for i in range(len(basket)):
        if basket[i] == bad_product:
            available_in_list = True
            break
    return available_in_list


def check_is_empty(baket):
    is_empty = False
    if len(basket) == 0:
        is_empty = True
    return is_empty



def buy(basket,sum,money):
    if money - sum >= 0:
        basket.clear()
        money = money - sum
        sum = 0
        print("Congrutilations!")
        print(f"Wallet: {money}")
    else:
        print("Sorry, you don't have enough money")
    return sum, money


def remove(basket,catalog,sum):
    product = input("name the product you want to remove :  ")
    if check_products(basket,product) == True:
        basket.remove(product)
        sum = sum - catalog[product]
        print(f"{product} was removed")
    else:
        print(f"{product} is not available")
    return sum

def exit(basket):
    if check_is_empty(basket) == False:
           print_basket(basket)
           basket.clear()
    else:
        print("your basket is empty")


catalog = {"table": 20, "bookcase": 30, "desk": 40, "fridge": 50, "bed": 35}
basket = []
money = 200
sum = 0

print("welcome to furniture shop")
while True:
    function = input(
        "choose the action:   show your catalog / show the product price / check my wallet / add the product / print my basket /  buy / remove / exit / show my sum : ")
    if function == "show the catalog":
        print_catalog(catalog)
    elif function == "check my wallet":
        print(f"Wallet: {money}")
    elif function == "show my basket":
        print_basket(basket)
    elif function == "show the product price":
        print_price(catalog)
    elif function == "add":
        sum = addition(catalog,basket,sum)
    elif function == "show my sum":
        print(f"Sum : {sum}")
    elif function == "buy":
        sum,money = buy(basket,sum,money)
    elif function == "remove":
        sum = remove(basket, catalog, sum)

    elif function == "exit":
        exit(basket)
        break


