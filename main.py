class Store(object):
    def __init__(self, name, address, items=None):
        self.name = name
        self.address = address
        self.items = items
    def add_item(self, name, price): #Добавление товара в магазин
        self.items[name] = price

    def remove_item(self, name): #Удаление товара из магазина
        del self.items[name]

    def get_item(self, name): #Получение цены товара
        return self.items[name]

    def update_item(self, name, price): #Обновление цены товара
        self.items[name] = price
    def goods(self):
        print(self.items)

shops = []
shops.append(Store('Перекресток', 'ул. Пушкина, д. 10', {'Молоко': 200, 'Кефир': 300}))
shops.append(Store('Пятерочка', 'ул. Ленина, д. 18', {'Яблоки': 200, 'Груша': 300}))
shops.append(Store('Магнит', 'ул. Глинки, д. 30', {'Хлеб': 200, 'Картофель': 300}))

shops[1].goods()
