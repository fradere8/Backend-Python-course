import datetime


class Product:
    def __init__(self, name: str, price: float, amount: int, category: str):
        self.name = name
        self.price = price
        self.amount = amount
        self.category = category
        
    def __str__(self):
        return f"{self.name} ({self.category}): {self.price} руб. Количество на складе: {self.amount}"
        
class Order:
    def __init__(
            self,
            date: datetime.date, 
            order_id: int, 
            products: list,  
            sale: float, 
            taxes: float
            ):
        
        self.order_id = order_id
        self.products = products
        self.sale = sale
        self.taxes = taxes
        self.date = date

    def calculate_total_price(self):
        """ Вычисляет общую стоимость заказа. """
        total = 0
        for product, quantity in self.products:
            total += product.price * quantity
        total -= total * self.sale
        total += total * self.taxes
        return total
    
    def __str__(self):
        return f"Заказ №{self.order_id} от {self.date}. " \
            f"Общая стоимость: {self.calculate_total_price()} руб."
    
class Customer:
    def __init__(self, name: str, phone: str, order_history: list):
        self.name = name
        self.phone = phone
        self.order_history = order_history
    
    def get_order_history(self):
        """ Возвращает историю заказов клиента. """
        return self.order_history
    
    def add_order(self, order: Order):
        """ Добавляет заказ в историю заказов клиента. """
        self.order_history.append(order)
        
    def __str__(self):
        return f"Имя: {self.name}, Телефон: {self.phone}"
    
class ShoppingCart:
    def __init__(self, customer: Customer):
        self.customer = customer
        self.items_in_cart = []
        
    def find_index(self, product: Product):
        for i, (p, q) in enumerate(self.items_in_cart):
            if p is product:
                return i
        return None
 
    def add_item(self, product: Product, quantity: int):
        """ Добавляет товар в корзину (если он уже есть, увеличивает количество). """
        idx = self.find_index(product)
        if idx is None:
            self.items_in_cart.append((product, quantity))
            return
        current_product_quantity = self.items_in_cart[idx][1]
        if product.amount < current_product_quantity + quantity:
            print(f"Недостаточно товара {product.name} на складе.")
            return
               
        self.items_in_cart[idx] = (product, current_product_quantity + quantity)
 
    def remove_item(self, product: Product):
        """ Удаляет товар из корзины. """
        idx = self.find_index(product)
        if idx is not None:
            self.items_in_cart.pop(idx)
 
    def update_quantity(self, product: Product, quantity: int):
        """ Задаёт новое количество товара в корзине. """
        idx = self.find_index(product)
        if idx is None:
            print(f"Товара {product.name} нет в корзине.")
            return
        if quantity <= 0:
            self.remove_item(product)
            return
        if product.amount < quantity:
            print(f"Недостаточно товара {product.name} на складе.")
            return
        self.items_in_cart[idx] = (product, quantity)
 
    def calculate_total(self):
        """ Вычисляет общую стоимость товаров в корзине. """
        return sum(product.price * quantity for product, quantity in self.items_in_cart)
 
    def checkout(self, sale: float, taxes: float):
        """ Оформляет заказ и возвращает объект Order. """
        if not self.items_in_cart:
            print("Корзина пуста.")
            return None
 
        for product, quantity in self.items_in_cart:
            if product.amount < quantity:
                print(f"Недостаточно товара {product.name} на складе.")
                return None
        for product, quantity in self.items_in_cart:
            product.amount -= quantity
 
        order = Order(
            date=datetime.date.today(),
            order_id=len(self.customer.order_history) + 1,
            products=list(self.items_in_cart),
            sale=sale,
            taxes=taxes
        )
        self.customer.add_order(order)
        self.items_in_cart.clear()
        return order
    
laptop = Product("Ноутбук", 80000, 15, "Электроника")
mouse = Product("Мышь", 1500, 30, "Аксессуары")

customer = Customer("Анна", "+7 999 999 99 99", [])
cart = ShoppingCart(customer)

cart.add_item(laptop, 1)
cart.add_item(mouse, 2)
cart.update_quantity(mouse, 3)
print("Сумма в корзине:", cart.calculate_total())

order = cart.checkout(sale=0.10, taxes=0.20)
print(order)
print(laptop)

print("История заказов клиента:")
for order in customer.get_order_history():
    print(order)    
    