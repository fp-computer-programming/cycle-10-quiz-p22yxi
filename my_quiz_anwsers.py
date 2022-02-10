# Yongdong Xi
prices = [30, 40, 25, 55, 60, 80, 65]
sales = [1, 3, 2, 5, 2, 1, 2]
items = [['tee-shirt','long-sleeved','tanktop'],['quarter-zip','pullover','full-zip','half-zip']]

def find_ave_price(price):
    total = 0
    for x in price:
        total += x
    ave_price = total / len(price)
    return ave_price


def less_price(price):
    lst = []
    for x in price:
        lst.append(x - 5)
    return lst


def revenue(price, sale):
    total = 0
    for index1, x in enumerate(price):
        for index2, r in enumerate(sale):
            if index1 == index2:
                s = x * r
                total += s
    return total


def new_price(price):
    for index, p in enumerate(price):
        if p > 40:
            newp = p * 0.9
        elif p <= 40:
            newp = p
        price[index] = newp
    return price


def food_costs(item_lst, price): 
    for item in item_lst:    
        for index, clothes in enumerate(item):
            item[index] = clothes + ' $' + str(price[0])
            del price[0]
        prices_and_items = item_lst
    return prices_and_items
    

print(food_costs(items, prices))