import sys
from decimal import Decimal

def main():
    exchange_file = input()
    amounts_file = input()

    rates = {}
    to_convert = []
    with open(exchange_file, encoding='utf-8') as exf:
        for line in exf:
            if len(line.strip('\n \t')) > 0:
               line_arr = line.strip('\n \t').split(' ')
               rates[line_arr[0]] = Decimal(line_arr[1])

    with open(amounts_file, encoding='utf-8') as amf:
        for line in amf:
             if len(line.strip('\n \t')) > 0:
               line_arr = line.strip('\n \t').split(' ')
               to_convert.append((Decimal(line_arr[0]), line_arr[1]))
    for amount, curr in to_convert:
        print('{0:.2f}'.format(amount/ rates[curr]))


if __name__ == "__main__":
    sys.exit(int(main() or 0))