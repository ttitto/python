from datetime import timezone
from entities import Sale
from logging import Logger
from decimal import Decimal

class Analyzer:

    def __init__(self, **kwargs):
        self.logger = Logger('Analyzer Logger', 1)

    def handle_sale(self, sale):
        pass

    def analyze(self):
        pass

class StarsChartAnalyzer(Analyzer):
    SCREEN_WIDTH = 40
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._max_value = 0
        self._min_value = 0
        self._longuest_key_name = 0
        self.max_stars_count = 0

    def handle_sale(self, sale):
        pass

    def analyze(self):
        pass

    def _set_stars_chart_values(self, key_length:int, current_value):
        if self._max_value <= current_value:
            self._max_value = current_value
        if self._min_value == 0 or self._min_value >= current_value:
            self._min_value = current_value
        if self._longuest_key_name <= key_length:
            self._longuest_key_name = key_length
        self.max_stars_count = StarsChartAnalyzer.SCREEN_WIDTH - self._longuest_key_name


class CommonAnalyzer(Analyzer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._sales_count = 0
        self._sales_sum = 0
        self._sales_total_average = 0
        self._begin_date = None
        self._end_date = None

    def handle_sale(self, sale):
        assert isinstance(sale, Sale)
        sale.sale_time = sale.sale_time.astimezone(timezone.utc)
        self._sales_count += 1
        self._sales_sum += sale.sale_total
        self._sales_total_average = self._sales_sum / self._sales_count
        if not self._begin_date:
            self._begin_date = sale.sale_time
        if not self._end_date:
            self._end_date = sale.sale_time
        if sale.sale_time <= self._begin_date:
            self._begin_date = sale.sale_time
        if sale.sale_time >= self._end_date:
            self._end_date = sale.sale_time
            
    def analyze(self):
        print('''
Summary
-------
Sales total count: {sales_count}
Sales total amount: {sales_sum}
Sales average amount: {sales_average}
Begin of data period: {sales_begin}
End of data period: {sales_end}'''.format(sales_count=self._sales_count, sales_sum=self._sales_sum, sales_average=self._sales_total_average, sales_begin=self._begin_date.astimezone(timezone.utc), sales_end=self._end_date.astimezone(timezone.utc)))

class SalesByCategoryAnalyzer(StarsChartAnalyzer):
    def __init__(self, items, **kwargs):
        super().__init__(**kwargs)
        self._items = items
        self._sales_by_category = {}

    def handle_sale(self, sale):
        assert isinstance(sale, Sale)
        assert isinstance(self._items, dict)

        if sale.item_id in self._items:
            category = self._items[sale.item_id].category
            if category in self._sales_by_category:
                self._sales_by_category[category] += sale.sale_total
            else:
                self._sales_by_category[category] = sale.sale_total

            super()._set_stars_chart_values(len(category), self._sales_by_category[category])

        else:
            self.logger.log(1, 'Item id {item_id} of a sale not corresponding to item id from the catalog'.format(item_id=sale.item_id))

    def analyze(self):
        print('Total sales sum by categories\n-----------------------------')
        for cat, price in sorted(self._sales_by_category.items(),key=lambda x: x[1], reverse=True)[:5]:
            print('''{category}:{padding}{stars} {total:.2f} E '''.format(category=cat, stars='*' * int(self.max_stars_count + self._sales_by_category[cat] * self.max_stars_count / self._max_value), total=self._sales_by_category[cat], padding=' ' * (self._longuest_key_name - len(cat))))


class SalesByTownAnalyzer(StarsChartAnalyzer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._sales_by_town = {}


    def handle_sale(self, sale):
        assert isinstance(sale, Sale)

        if sale.city not in self._sales_by_town:
            self._sales_by_town[sale.city] = Decimal('0')
        self._sales_by_town[sale.city] += sale.sale_total

        super()._set_stars_chart_values(len(sale.city), self._sales_by_town[sale.city])
        

    def analyze(self):
        print('Total sales sum by towns\n-----------------------------')
        for t, price in sorted(self._sales_by_town.items(), key=lambda x: x[1], reverse=True)[:5]:
            print('{town}:{padding}{stars} {total:.2f} E'.format(town=t, stars='*' * int(self._sales_by_town[t] * self.max_stars_count / self._max_value), total=self._sales_by_town[t], padding=' ' * (self._longuest_key_name - len(t))))

class SalesByUtcHoursAnalyzer(StarsChartAnalyzer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self._sales_by_hour = {}


    def handle_sale(self, sale):
        assert isinstance(sale, Sale)

        utc_hour = sale.sale_time.astimezone(timezone.utc)
        utc_hour = utc_hour.replace(second=0, microsecond = 0, minute=0)
        if utc_hour not in self._sales_by_hour:
            self._sales_by_hour[utc_hour] = Decimal('0')
        self._sales_by_hour[utc_hour] += sale.sale_total
        super()._set_stars_chart_values(15, self._sales_by_hour[utc_hour])


    def analyze(self):
        print('Total sales sum by UTC Hour\n--------------------------- ')
        for h, price in sorted(self._sales_by_hour.items(), key=lambda x: x[1], reverse=True)[:5]:
            print('''{hour} :{padding}{stars} {total:.2f} E '''.format(hour=h.strftime('%Y-%m-%d %H:%M'), stars='*' * int(self.max_stars_count + self._sales_by_hour[h] * self.max_stars_count / self._max_value), total=self._sales_by_hour[h], padding=' ' * (self._longuest_key_name - 15)))
