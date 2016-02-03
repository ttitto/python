import sys
def get_prices_from_file(filepath):
    prices = []
    with open(filepath, 'r') as f:
        for line_number, line_content in enumerate(f):
            try:
                price_float = float(line_content.rstrip().split(',')[-1])
                prices.append(price_float)
            except:
                print('Price on row {row} not convertable to float. This price is not included in result'.format(row = line_number + 1))
    return prices


def average_price_from_file(prices) -> float:
    average = sum(prices) / float(len(prices))
    return average


def main():
    prices = get_prices_from_file('./data/catalog_sample.csv')
    average_price = average_price_from_file(prices)
    print('Average price: {:.2f}'.format(average_price))

    prices = get_prices_from_file('./data/catalog_full.csv')
    average_price = average_price_from_file(prices)
    print('Average price: {:.2f}'.format(average_price))

if __name__ == "__main__":
    sys.exit(int(main() or 0))