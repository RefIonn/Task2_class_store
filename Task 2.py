class ItemNotFoundError(Exception):
    def __init__(self, item_name):
        super().__init__(f"Товара или количество запрашиваемого товара {item_name} нет в наличии.")


class Warehouse:
    def __init__(self, item_name, quantity):
        self.item_name = item_name
        self.items = {} # Словарь с товарами
        self.add_item(item_name, quantity)

    def add_item(self, item_name, quantity):
        if item_name in self.items:
            self.items[item_name] += quantity
        else:
            self.items[item_name] = quantity

    def purchase_item(self, item_name, quantity):
        if item_name in self.items and self.items[item_name] >= quantity: #Идёт проверка на то, есть ли товар в словаре, и на то, есть ли такое количество имеющегося товара
            self.items[item_name] -= quantity #Если условие выполняется, то количество товара в self.items[item_name]
                                              # больше или равно quantity, то в этой строчке вычитается приобритённое количество товара
            print(f"Покупка совершена! Товар - {item_name} в количестве {quantity} шт.") #Если условие выполняется - покупка совершается
        else:
            raise ItemNotFoundError(item_name) #Выводится ошибка о неизвестном товаре или недоступном его количестве


Warehouse1 = Warehouse('Хлеб', 20)
Warehouse2 = Warehouse('Молоко', 13)
Warehouse3 = Warehouse('Чипсы', 3)
try:
    Warehouse1.purchase_item('Хлеб', 11)
    Warehouse2.purchase_item('Молоко', 12)
    Warehouse3.purchase_item('Чипсы', 10)
except ItemNotFoundError as Except:
    print(Except)