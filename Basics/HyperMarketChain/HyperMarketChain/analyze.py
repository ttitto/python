import sys
import os
import logging
import iso8601
from decimal import Decimal
from loaders import CsvLoader, JsonLoader, YamlLoader
from entities import Item, Sale
from analyzers import CommonAnalyzer, SalesByCategoryAnalyzer, SalesByTownAnalyzer, SalesByUtcHoursAnalyzer

def main():
    LOADERS = {
        '.json':JsonLoader,
        '.yaml': YamlLoader,
        '.csv': CsvLoader
    }

    logger = logging.Logger(name='simple logger')
    if not os.access(sys.argv[1], os.R_OK) or not os.path.isfile(sys.argv[1]):
        logger.log('Catalog file is not accessible: {}'.format(sys.argv[1]))
    if not os.access(sys.argv[2], os.R_OK) or not os.path.isfile(sys.argv[2]):
        logger.log('Sales file is not accessible: {}'.format(sys.argv[2]))
    
    _, extension = os.path.splitext(sys.argv[1])
    catalog = LOADERS[extension](file_path=sys.argv[1]).load()
    items = parse_catalog(catalog, logger)
    _, extension = os.path.splitext(sys.argv[2])
    sales_data = LOADERS[extension](file_path = sys.argv[2]).load()
    sales = parse_sales(sales_data, logger)

    all_analyzers = []
    common_analyzer = CommonAnalyzer()
    by_category_analyzer = SalesByCategoryAnalyzer(items)
    by_town_analyzer = SalesByTownAnalyzer()
    by_utc_hour_analyzer = SalesByUtcHoursAnalyzer()

    all_analyzers.append(common_analyzer)
    all_analyzers.append(by_category_analyzer)
    all_analyzers.append(by_town_analyzer)
    all_analyzers.append(by_utc_hour_analyzer)

    for s in sales:
        for an in all_analyzers:
            an.handle_sale(s)

    for an in all_analyzers:
        an.analyze()


def parse_catalog(catalog, logger:logging.Logger):
    items = {}
    for row in catalog:
        if len(row) != 8:
            logger.log('Row contains invalid count of arguments: {}'.format(row))
        item = {}
        try:
            item['id'] = row[0]
            item['name'] = row[1]
            item['colors'] = row[2].split(sep='/')
            item['group'] = row[3]
            item['sport'] = row[4]
            item['category'] = row[5]
            item['subcategory'] = row[6]
            item['gender'] = row[7]
        except Exception as e:
            logger.log(1, 'Row''s data can not be parse to Item object: {}'.format(row))
            continue
        items[item['id']] = Item(**item)
    return items


def parse_sales(sales_data:list, logger: logging.Logger):
    sales = []
    for row in sales_data:
        if len(row) != 5:
            logger.log('Row contains invalid count of arguments: {}'.format(row))
        sale = {}
        try:
            sale['item_id'] = row[0]
            sale['country'] = row[1]
            sale['city'] = row[2]
            sale['sale_time'] = iso8601.parse_date(row[3])
            sale['sale_total'] = Decimal(row[4])
        except Exception:
            logger.log(1, 'Row''s data can not be parse to Item object: {}'.format(row))
            continue
        sales.append(Sale(**sale))
    return sales



if __name__ == "__main__":
    sys.exit(int(main() or 0))