class Product:
    """
    Класс для представления товара в интернет-магазине.
    """

    def __init__(self, name: str, description: str, price: float, quantity: int):
        """
        Инициализация объекта товара.

        Args:
            name: Название товара
            description: Описание товара
            price: Цена товара
            quantity: Количество товара в наличии
        """
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

    def __str__(self):
        """Строковое представление продукта."""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Магический метод сложения для продуктов.

        Returns:
            Сумма произведений цены на количество для двух продуктов
        """
        if not isinstance(other, Product):
            raise TypeError("Можно складывать только объекты класса Product")

        return (self.__price * self.quantity) + (other.__price * other.quantity)

    @property
    def price(self):
        """Геттер для цены."""
        return self.__price

    @price.setter
    def price(self, new_price: float):
        """
        Сеттер для цены с проверкой на положительное значение.

        Args:
            new_price: Новая цена товара
        """
        if new_price <= 0:
            print("Цена не должна быть нулевая или отрицательная")
        else:
            self.__price = new_price

    @classmethod
    def new_product(cls, product_data: dict):
        """
        Класс-метод для создания нового продукта из словаря.

        Args:
            product_data: Словарь с данными продукта

        Returns:
            Объект класса Product
        """
        return cls(
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            quantity=product_data["quantity"],
        )

    def __repr__(self):
        """Представление объекта для отладки."""
        return f"Product('{self.name}', '{self.description}', {self.__price}, {self.quantity})"


class Category:
    """
    Класс для представления категории товаров в интернет-магазине.
    """

    category_count = 0
    product_count = 0

    def __init__(self, name: str, description: str, products: list):
        """
        Инициализация объекта категории.

        Args:
            name: Название категории
            description: Описание категории
            products: Список товаров в категории
        """
        self.name = name
        self.description = description
        self._products = products

        # Обновляем атрибуты класса
        Category.category_count += 1
        Category.product_count += len(products)

    def __str__(self):
        """Строковое представление категории."""
        total_quantity = sum(product.quantity for product in self._products)
        return f"{self.name}, количество продуктов: {total_quantity} шт."

    def add_product(self, product):
        """
        Добавляет продукт в категорию.

        Args:
            product: Объект класса Product для добавления
        """
        if isinstance(product, Product):
            self._products.append(product)
            Category.product_count += 1
        else:
            raise TypeError("Можно добавлять только объекты класса Product")

    @property
    def products(self):
        """Геттер для списка товаров в формате строк."""
        products_list = []
        for product in self._products:
            products_list.append(str(product))
        return "\n".join(products_list)

    def __len__(self):
        """Возвращает количество товаров в категории."""
        return len(self._products)

    def __iter__(self):
        """Возвращает итератор для товаров категории."""
        return CategoryIterator(self._products)

    @classmethod
    def reset_counters(cls):
        """Сбрасывает счетчики категорий и продуктов."""
        cls.category_count = 0
        cls.product_count = 0

    def __repr__(self):
        """Представление объекта для отладки."""
        return f"Category('{self.name}', '{self.description}', {len(self._products)} products)"


class CategoryIterator:
    """
    Итератор для перебора товаров в категории.
    """

    def __init__(self, products: list):
        """
        Инициализация итератора.

        Args:
            products: Список товаров для итерации
        """
        self._products = products
        self._index = 0

    def __iter__(self):
        """Возвращает сам итератор."""
        return self

    def __next__(self):
        """
        Возвращает следующий товар в категории.

        Returns:
            Следующий объект Product

        Raises:
            StopIteration: когда товары закончились
        """
        if self._index < len(self._products):
            product = self._products[self._index]
            self._index += 1
            return product
        else:
            raise StopIteration
