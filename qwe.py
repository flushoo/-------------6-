class Product:
    def __init__(self, name, price, stock):
        self.name = name  # Название товара
        self.price = price  # Цена товара
        self.stock = stock  # Количество на складе

    def show_info(self):
        # Отображаем информацию о товаре
        print(f"Товар: {self.name}, Цена: {self.price} руб., Остаток на складе: {self.stock}")


class Cart:
    def __init__(self):
        self.items = []  # Список товаров в корзине

    def add_to_cart(self, product, quantity):
        # Добавляем товар в корзину
        if product.stock >= quantity:
            self.items.append({'product': product, 'quantity': quantity})
            product.stock -= quantity  # Уменьшаем количество товара на складе
            print(f"{quantity} единиц товара '{product.name}' добавлено в корзину.")
        else:
            print(f"Ошибка: недостаточно товара '{product.name}' на складе.")

    def remove_from_cart(self, product):
        # Удаляем товар из корзины
        for item in self.items:
            if item['product'] == product:
                self.items.remove(item)
                product.stock += item['quantity']  # Восстанавливаем количество товара на складе
                print(f"Товар '{product.name}' удалён из корзины.")
                return
        print(f"Товар '{product.name}' не найден в корзине.")

    def show_cart(self):
        # Выводим список товаров в корзине
        if not self.items:
            print("Ваша корзина пуста.")
            return

        total_price = 0
        print("Содержимое корзины:")
        for item in self.items:
            product = item['product']
            quantity = item['quantity']
            print(f"Товар: {product.name}, Количество: {quantity}, Стоимость: {product.price * quantity} руб.")
            total_price += product.price * quantity
        print(f"Общая стоимость: {total_price} руб.")


class Store:
    def __init__(self):
        self.products = []  # Список доступных товаров

    def add_product(self, product):
        # Добавляем товар в магазин
        self.products.append(product)

    def show_products(self):
        # Показываем все доступные товары в магазине
        if not self.products:
            print("В магазине нет товаров.")
            return

        print("Доступные товары в магазине:")
        for product in self.products:
            product.show_info()

    def process_order(self, cart):
        # Обрабатываем заказ, уменьшая количество товаров на складе
        for item in cart.items:
            product = item['product']
            quantity = item['quantity']
            if product.stock < 0:
                print(f"Ошибка: товар '{product.name}' не может быть обработан.")
                return
        print("Заказ успешно обработан.")