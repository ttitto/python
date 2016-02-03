class Item:
    def __init__(self, **kwargs):
        self.id = kwargs['id']
        self.name = kwargs['name']
        self.colors = kwargs['colors']
        self.group = kwargs['group']
        self.sport = kwargs['sport']
        self.category = kwargs['category']
        self.subcategory = kwargs['subcategory']
        self.gender = kwargs['gender']

class Sale:
    def __init__(self, **kwargs):
        self.item_id = kwargs['item_id']  
        self.country = kwargs['country']  
        self.city = kwargs['city'] 
        self.sale_time = kwargs['sale_time'] 
        self.sale_total = kwargs['sale_total']