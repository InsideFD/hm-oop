from abc import ABC, abstractmethod


class LoggingMixin:
    """
    Миксин для логирования создания объектов.
    """

    def __init__(self, *args, **kwargs):
        """
        Инициализация с логированием параметров создания объекта.
        """
        # Сначала вызываем следующий конструктор в цепочке
        super().__init__(*args, **kwargs)


class BaseProduct(ABC):
    """
    Абстрактный базовый класс для товаров.
    """

    @abstractmethod
    def __init__(self):
        """
        Абстрактный метод инициализации продукта.
        """
        pass

    @abstractmethod
    def __str__(self):
        """Абстрактный метод строкового представления."""
        pass

    @abstractmethod
    def __add__(self, other):
        """Абстрактный метод сложения продуктов."""
        pass

    @property
    @abstractmethod
    def price(self):
        """Абстрактный геттер для цены."""
        pass

    @price.setter
    @abstractmethod
    def price(self, value):
        """Абстрактный сеттер для цены."""
        pass


class Product(LoggingMixin, BaseProduct):
    """
    Класс для представления товара в интернет-магазине.
    Наследуется от миксина LoggingMixin и абстрактного класса BaseProduct.
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
        # Инициализируем атрибуты
        self.name = name
        self.description = description
        self.__price = price
        self.quantity = quantity

        # Вызываем конструкторы родителей через super()
        super().__init__()

        # Логируем создание объекта с параметрами
        print(
            f"Создан объект Product с параметрами: Product('{name}', '{description}', {price}, {quantity})"
        )

    def __str__(self):
        """Строковое представление продукта."""
        return f"{self.name}, {self.__price} руб. Остаток: {self.quantity} шт."

    def __add__(self, other):
        """
        Магический метод сложения для продуктов.

        Returns:
            Сумма произведений цены на количество для двух продуктов

        Raises:
            TypeError: если пытаются сложить товары разных классов
        """
        if type(self) is not type(other):
            raise TypeError("Нельзя складывать товары разных классов")

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


class Smartphone(Product):
    """
    Класс для представления смартфона.
    Наследуется от класса Product.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        efficiency: float,
        model: str,
        memory: int,
        color: str,
    ):
        """
        Инициализация объекта смартфона.

        Args:
            name: Название смартфона
            description: Описание смартфона
            price: Цена смартфона
            quantity: Количество в наличии
            efficiency: Производительность
            model: Модель
            memory: Объем встроенной памяти (ГБ)
            color: Цвет
        """
        # Инициализируем родительский класс
        super().__init__(name, description, price, quantity)
        # Добавляем специфичные атрибуты
        self.efficiency = efficiency
        self.model = model
        self.memory = memory
        self.color = color

        # Логируем создание объекта с параметрами
        params = f"'{name}', '{description}', {price}, {quantity}, {efficiency}, '{model}', {memory}, '{color}'"
        print(f"Создан объект Smartphone с параметрами: Smartphone({params})")

    def __repr__(self):
        """Представление объекта для отладки."""
        return (
            f"Smartphone('{self.name}', '{self.description}', {self.price}, "
            f"{self.quantity}, {self.efficiency}, '{self.model}', {self.memory}, '{self.color}')"
        )


class LawnGrass(Product):
    """
    Класс для представления газонной травы.
    Наследуется от класса Product.
    """

    def __init__(
        self,
        name: str,
        description: str,
        price: float,
        quantity: int,
        country: str,
        germination_period: int,
        color: str,
    ):
        """
        Инициализация объекта газонной травы.

        Args:
            name: Название травы
            description: Описание травы
            price: Цена травы
            quantity: Количество в наличии
            country: Страна-производитель
            germination_period: Срок прорастания (дни)
            color: Цвет
        """
        # Инициализируем родительский класс
        super().__init__(name, description, price, quantity)
        # Добавляем специфичные атрибуты
        self.country = country
        self.germination_period = germination_period
        self.color = color

        # Логируем создание объекта с параметрами
        params = f"'{name}', '{description}', {price}, {quantity}, '{country}', {germination_period}, '{color}'"
        print(f"Создан объект LawnGrass с параметрами: LawnGrass({params})")

    def __repr__(self):
        """Представление объекта для отладки."""
        return (
            f"LawnGrass('{self.name}', '{self.description}', {self.price}, "
            f"{self.quantity}, '{self.country}', {self.germination_period}, '{self.color}')"
        )


class Category:
    """
    Класс для представления категории товаров в интернет-магазине.
    """

    # Атрибуты класса
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
            product: Объект для добавления (должен быть Product или его наследником)

        Raises:
            TypeError: если переданный объект не является продуктом
        """
        if not isinstance(product, Product):
            raise TypeError(
                "Можно добавлять только объекты класса Product или его наследников"
            )

        self._products.append(product)
        Category.product_count += 1

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


class Order:
    """
    Класс для представления заказа.
    """

    def __init__(self, product: Product, quantity: int):
        """
        Инициализация заказа.

        Args:
            product: Товар в заказе
            quantity: Количество товара
        """
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity

    def __str__(self):
        """Строковое представление заказа."""
        return (
            f"Заказ: {self.product.name}, "
            f"Количество: {self.quantity}, "
            f"Итого: {self.total_price} руб."
        )

    def __repr__(self):
        """Представление объекта для отладки."""
        return f"Order({repr(self.product)}, {self.quantity})"
