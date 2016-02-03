import sys
from io import TextIOWrapper
def get_categorized_prices_from_file(filepath :str) -> dict:
    prices = {}
    try:
        with open(filepath, 'r') as f:
            assert isinstance(f, TextIOWrapper)
            for line_number, line_content in enumerate(f):
                try:
                    if line_content and len(line_content.rstrip('\n')) > 0:
                        splitted_line = line_content.rstrip('\n').split(',')
                        category = splitted_line[-2]
                        price_float = float(splitted_line[-1])
                        if category in prices:
                            prices[category].append(price_float)
                        else:
                            prices[category] = [price_float]
                except ValueError:
                    print('Price on row {row} not convertable to float. This price is not included in result'.format(row = line_number + 1))
    except IOError:
        print("Failed to open data file.")
    return prices


def average_prices_from_file(prices :dict) -> dict:
    average_prices = {}
    for key in prices:
        average_prices[key] = sum(prices[key]) / float(len(prices[key]))
    return average_prices


def print_categorized_average_prices(average_prices :dict):
    for key in average_prices:
        print('{} - average price: {:.2f}'.format(key, average_prices[key]))


def main():
    prices = get_categorized_prices_from_file('./data/catalog_sample.csv')
    average_prices = average_prices_from_file(prices)
    print_categorized_average_prices(average_prices)
    print('\n')
    prices = get_categorized_prices_from_file('./data/catalog_full.csv')
    average_price = average_prices_from_file(prices)
    print_categorized_average_prices(average_price)

if __name__ == "__main__":
    sys.exit(int(main() or 0))