import sys
from decimal import Decimal

def main():
    id = input()
    sales_file = input()

    sales_by_id = {}
    with open(sales_file, encoding='utf-8') as f:
        for l in f:
            if len(l.strip('\n\t\r ')) > 0:
                line = l.strip('\n\t\r ').split(',')
                current_price = Decimal(line[4])
                key = line[0].replace('"', '')
                current_city = line[2].replace('"', '')
                if key not in sales_by_id:
                    sales_by_id[key] = (current_city, current_price)
                else:
                    if current_price < sales_by_id[key][1]:
                        sales_by_id[key] = (current_city, current_price)
    print(sales_by_id[id][0])
    

if __name__ == "__main__":
    sys.exit(int(main() or 0))