def average_price():
    price = input("Insert price: ")
    prices = []
    while price != 'stop':
        try:
            prices.append(float(price))
        except ValueError:
            print('Please insert valid number!')
        price = input("Insert price: ")
    prices.sort()
    lowest = prices.pop(0)
    highest = prices.pop()
    for i in prices:
        if i == lowest or i == highest:
            prices.remove(i)
    if len(prices) > 3:
        average = sum(prices) / float(len(prices))
        print('highest price: {}, lowest price: {}, average price: {}'.format(highest, lowest, average))
    else:
        print('Not enough prices to calculate average price')


average_price()
