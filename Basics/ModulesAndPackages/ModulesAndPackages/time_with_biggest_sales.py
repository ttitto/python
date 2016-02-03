from io import TextIOWrapper
from datetime import datetime
import logging

def get_categorized_prices(filepath: str, throw_on_error: bool=False) -> (dict, dict):
    prices_per_weekdays = {}
    prices_per_hour = {}
    if not throw_on_error:
        logger = logging.getLogger()
    with open(filepath, 'r') as f:
        assert isinstance(f, TextIOWrapper)
        for line_number, line_content in enumerate(f):
            if line_content:
                stripped = line_content.rstrip('\n')
                if len(stripped) > 0:
                    splitted_line = stripped.split(',')
                    try:
                        current_dt = datetime.strptime(splitted_line[0], '%Y-%m-%d %H:%M:%S')
                        current_weekday = current_dt.strftime('%a')
                        current_time = current_dt.strftime('%H')
                    except ValueError:
                        if throw_on_error:
                            raise ValueError(message = 'String can not be parsed to datetime on row {}'.format(line_number))
                        else:
                            logger.warn(msg='String can not be parsed to datetime on row {}'.format(line_number))
                            continue
                    try:
                        current_price = float(splitted_line[1])
                    except ValueError:
                        if throw_on_error:
                            raise ValueError(message = 'String can not be parsed to float on row {}'.format(line_number))
                        else:
                            logger.warn(msg='String can not be parsed to float on row {}'.format(line_number))
                            continue
                    except IndexError:
                        if throw_on_error:
                            raise IndexError(message = 'Line {} does not contain any value for price'.format(line_number))
                        else:
                            logger.warn(msg='Line {} does not contain any value for price'.format(line_number))
                    if current_weekday not in prices_per_weekdays:
                        prices_per_weekdays[current_weekday] = 0
                    prices_per_weekdays[current_weekday] += current_price
                    if current_time not in prices_per_hour:
                        prices_per_hour[current_time] = 0
                    prices_per_hour[current_time] += current_price

                    
                else:
                    if throw_on_error:
                        raise ValueError('Line {} contains only insignificant characters.'.format(line_number))
                    else:
                        logger.warn(msg='Line {} contains only insignificant characters.'.format(line_number))
                        continue
            else:
                if throw_on_error:
                    raise ValueError('Line {} is empty.'.format(line_number))
                else:
                    logger.warn(msg='Line {} is empty.'.format(line_number))
                    continue
    return (prices_per_hour, prices_per_weekdays)



(prices_per_hour, prices_per_weekday) = get_categorized_prices('./data/sales.csv')
max = []
max.append(0)
for hour in prices_per_hour:
    price = prices_per_hour[hour]
    print('{} --- {:.2f}'.format(hour, price))
    if price > max[0]:
        max.clear()
        max.append(price)
        max.append(hour)
    elif price == max[0]:
        max.append(hour)
print('=' * 30)
print('Max sales total {max_sales_total:.2f} is in the hour starting at {hours} o\'clock'.format(max_sales_total=max[0], hours =' and'.join(max[1:])))
print('=' * 30)

max = []
max.append(0)
for day, price in prices_per_weekday.items():
    print('{} --- {:.2f}'.format(day, price))
    if price > max[0]:
        max.clear()
        max.append(price)
        max.append(day)
    elif price == max[0]:
        max.append(hour)
print('=' * 30)
print('Max sales total {max_sales_total:.2f} were on {days}.'.format(max_sales_total=max[0], days =' and'.join(max[1:])))
print('=' * 30)