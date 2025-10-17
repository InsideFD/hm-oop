import pytest

from src.models import (BaseProduct, Category, LawnGrass, LoggingMixin, Order,
                        Product, Smartphone)


class TestAbstractClassesAndMixins:
    """Тесты для абстрактных классов и миксинов."""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом."""
        Category.reset_counters()

    def test_base_product_is_abstract(self):
        """Тест BaseProduct является абстрактным классом."""
        with pytest.raises(TypeError):
            _ = BaseProduct()

    def test_product_inherits_from_base_product(self):
        """Тест что Product наследуется от BaseProduct."""
        product = Product("Test Product", "Description", 100.0, 5)

        assert isinstance(product, BaseProduct)
        assert issubclass(Product, BaseProduct)

    def test_smartphone_inherits_from_product(self):
        """Тест что Smartphone наследуется от Product."""
        smartphone = Smartphone(
            name="Phone",
            description="Desc",
            price=50000.0,
            quantity=2,
            efficiency=3.0,
            model="A",
            memory=128,
            color="Black",
        )

        assert isinstance(smartphone, Product)
        assert isinstance(smartphone, BaseProduct)
        assert issubclass(Smartphone, Product)
        assert smartphone.efficiency == 3.0
        assert smartphone.model == "A"
        assert smartphone.memory == 128
        assert smartphone.color == "Black"

    def test_lawn_grass_inherits_from_product(self):
        """Тест что LawnGrass наследуется от Product."""
        lawn_grass = LawnGrass(
            name="Grass",
            description="Desc",
            price=1000.0,
            quantity=50,
            country="Russia",
            germination_period=10,
            color="Green",
        )

        assert isinstance(lawn_grass, Product)
        assert isinstance(lawn_grass, BaseProduct)
        assert issubclass(LawnGrass, Product)
        assert lawn_grass.country == "Russia"
        assert lawn_grass.germination_period == 10
        assert lawn_grass.color == "Green"

    def test_logging_mixin_functionality(self, capsys):
        """Тест функциональности миксина логирования."""
        _ = Product("Test Product", "Description", 100.0, 5)

        captured = capsys.readouterr()
        assert "Создан объект Product" in captured.out

    def test_logging_mixin_in_smartphone(self, capsys):
        """Тест миксин работает в Smartphone."""
        smartphone = Smartphone(
            name="Phone",
            description="Desc",
            price=50000.0,
            quantity=2,
            efficiency=3.0,
            model="A",
            memory=128,
            color="Black",
        )

        captured = capsys.readouterr()
        assert "Создан объект Smartphone" in captured.out
        assert smartphone.efficiency == 3.0
        assert smartphone.model == "A"

    def test_logging_mixin_in_lawn_grass(self, capsys):
        """Тест миксин работает в LawnGrass."""
        lawn_grass = LawnGrass(
            name="Grass",
            description="Desc",
            price=1000.0,
            quantity=50,
            country="Russia",
            germination_period=10,
            color="Green",
        )

        captured = capsys.readouterr()
        assert "Создан объект LawnGrass" in captured.out
        assert lawn_grass.country == "Russia"
        assert lawn_grass.germination_period == 10

    def test_product_inheritance_chain(self):
        """Тест цепочки наследования Product."""
        mro = Product.__mro__
        assert LoggingMixin in mro
        assert BaseProduct in mro
        assert Product in mro

    def test_abstract_methods_implementation(self):
        """Тест все абстрактные методы реализованы."""
        product = Product("Test", "Description", 100.0, 5)

        assert str(product) == "Test, 100.0 руб. Остаток: 5 шт."
        assert product.price == 100.0

        product2 = Product("Test2", "Description2", 200.0, 3)
        result = product + product2
        assert result == (100.0 * 5) + (200.0 * 3)


class TestOrderClass:
    """Тесты для класса Order (дополнительное задание)."""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом."""
        Category.reset_counters()

    def test_order_creation(self):
        """Тест создания заказа."""
        product = Product("Test Product", "Description", 100.0, 10)
        order = Order(product, 3)

        assert order.product == product
        assert order.quantity == 3
        assert order.total_price == 300.0  # 100 * 3

    def test_order_with_smartphone(self):
        """Тест создания заказа со смартфоном."""
        smartphone = Smartphone(
            name="Phone",
            description="Desc",
            price=50000.0,
            quantity=2,
            efficiency=3.0,
            model="A",
            memory=128,
            color="Black",
        )
        order = Order(smartphone, 1)

        assert order.product == smartphone
        assert order.total_price == 50000.0

    def test_order_with_lawn_grass(self):
        """Тест создания заказа с газонной травой."""
        lawn_grass = LawnGrass(
            name="Grass",
            description="Desc",
            price=1000.0,
            quantity=50,
            country="Russia",
            germination_period=10,
            color="Green",
        )
        order = Order(lawn_grass, 10)

        assert order.product == lawn_grass
        assert order.total_price == 10000.0  # 1000 * 10

    def test_order_string_representation(self):
        """Тест строкового представления заказа."""
        product = Product("Test Product", "Description", 100.0, 10)
        order = Order(product, 3)

        order_str = str(order)
        expected = "Заказ: Test Product, Количество: 3, Итого: 300.0 руб."
        assert order_str == expected

    def test_order_repr(self):
        """Тест представления заказа для отладки."""
        product = Product("Test Product", "Description", 100.0, 10)
        order = Order(product, 3)

        order_repr = repr(order)
        assert "Order(" in order_repr
        assert "Product('Test Product'" in order_repr
        assert "3" in order_repr


class TestCoverageImprovement:

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом."""
        Category.reset_counters()

    def test_product_repr_method(self):
        """Тест метода __repr__ для Product."""
        product = Product("Test", "Description", 100.0, 5)
        repr_str = repr(product)
        expected = "Product('Test', 'Description', 100.0, 5)"
        assert repr_str == expected

    def test_smartphone_repr_method(self):
        """Тест метода __repr__ для Smartphone."""
        smartphone = Smartphone(
            name="Phone",
            description="Desc",
            price=50000.0,
            quantity=2,
            efficiency=3.0,
            model="A",
            memory=128,
            color="Black",
        )
        repr_str = repr(smartphone)
        assert "Smartphone(" in repr_str
        assert "Phone" in repr_str
        assert "A" in repr_str

    def test_lawn_grass_repr_method(self):
        """Тест метода __repr__ для LawnGrass."""
        lawn_grass = LawnGrass(
            name="Grass",
            description="Desc",
            price=1000.0,
            quantity=50,
            country="Russia",
            germination_period=10,
            color="Green",
        )
        repr_str = repr(lawn_grass)
        assert "LawnGrass(" in repr_str
        assert "Grass" in repr_str
        assert "Russia" in repr_str

    def test_category_repr_method(self):
        """Тест метода __repr__ для Category."""
        category = Category("Test Category", "Description", [])
        repr_str = repr(category)
        expected = "Category('Test Category', 'Description', 0 products)"
        assert repr_str == expected

    def test_order_repr_method(self):
        """Тест метода __repr__ для Order."""
        product = Product("Test Product", "Description", 100.0, 10)
        order = Order(product, 3)
        repr_str = repr(order)
        assert "Order(" in repr_str
        assert "Product('Test Product'" in repr_str

    def test_product_price_setter_positive(self):
        """Тест сеттера цены с положительным значением."""
        product = Product("Test", "Description", 100.0, 5)
        product.price = 150.0
        assert product.price == 150.0

    def test_product_price_setter_negative_message(self, capsys):
        """Тест сообщения при установке отрицательной цены."""
        product = Product("Test", "Description", 100.0, 5)
        product.price = -50.0

        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 100.0  # Цена не изменилась

    def test_product_price_setter_zero_message(self, capsys):
        """Тест сообщения при установке нулевой цены."""
        product = Product("Test", "Description", 100.0, 5)
        product.price = 0.0

        captured = capsys.readouterr()
        assert "Цена не должна быть нулевая или отрицательная" in captured.out
        assert product.price == 100.0  # Цена не изменилась

    def test_add_product_with_invalid_type(self):
        """Тест добавления неверного типа в категорию."""
        category = Category("Test Category", "Description", [])

        with pytest.raises(
            TypeError,
            match="Можно добавлять только объекты класса Product или его наследников",
        ):
            category.add_product("invalid product")

    def test_category_iterator_stop_iteration(self):
        """Тест StopIteration в итераторе категории."""
        category = Category("Test Category", "Description", [])
        iterator = iter(category)

        with pytest.raises(StopIteration):
            next(iterator)

    def test_logging_mixin_with_parameters(self, capsys):
        """Тест что миксин выводит параметры при создании объекта."""
        _ = Product("Test Product", "Description", 100.0, 5)

        captured = capsys.readouterr()
        # Теперь проверяем новый формат вывода
        assert (
            "Создан объект Product с параметрами: Product('Test Product', 'Description', 100.0, 5)"
            in captured.out
        )

    def test_logging_mixin_inheritance_chain(self, capsys):
        """Тест миксин работает во всей цепочке наследования."""
        smartphone = Smartphone(
            name="Phone",
            description="Desc",
            price=50000.0,
            quantity=2,
            efficiency=3.0,
            model="A",
            memory=128,
            color="Black",
        )

        captured = capsys.readouterr()
        assert (
            "Создан объект Smartphone с параметрами: Smartphone('Phone', 'Desc', 50000.0, 2, 3.0, 'A', 128, 'Black')"
            in captured.out
        )
        assert smartphone.efficiency == 3.0
        assert smartphone.model == "A"

    def test_product_class_method_new_product(self):
        """Тест класс-метода new_product."""
        product_data = {
            "name": "New Product",
            "description": "New Description",
            "price": 150.0,
            "quantity": 10,
        }
        product = Product.new_product(product_data)

        assert product.name == "New Product"
        assert product.description == "New Description"
        assert product.price == 150.0
        assert product.quantity == 10

    def test_category_counters_after_multiple_operations(self):
        """Тест счетчиков после нескольких операций."""
        Category.reset_counters()

        initial_category_count = Category.category_count
        initial_product_count = Category.product_count

        product1 = Product("P1", "D1", 100.0, 1)
        product2 = Product("P2", "D2", 200.0, 2)

        category1 = Category("Cat1", "Desc1", [product1])
        _ = Category(
            "Cat2", "Desc2", [product2]
        )  # Используем _ для неиспользуемой переменной

        product3 = Product("P3", "D3", 300.0, 3)
        category1.add_product(product3)

        assert Category.category_count == initial_category_count + 2
        assert Category.product_count == initial_product_count + 3

    def test_order_total_price_calculation(self):
        """Тест расчета общей стоимости заказа."""
        product = Product("Test Product", "Description", 100.0, 10)
        order = Order(product, 3)

        assert order.total_price == 300.0  # 100 * 3

    def test_order_string_representation(self):
        """Тест строкового представления заказа."""
        product = Product("Test Product", "Description", 100.0, 10)
        order = Order(product, 3)

        order_str = str(order)
        expected = "Заказ: Test Product, Количество: 3, Итого: 300.0 руб."
        assert order_str == expected

    def test_lawn_grass_logging(self, capsys):
        lawn_grass = LawnGrass(
            name="Grass",
            description="Desc",
            price=1000.0,
            quantity=50,
            country="Russia",
            germination_period=10,
            color="Green",
        )

        captured = capsys.readouterr()
        assert (
            "Создан объект LawnGrass с параметрами: LawnGrass('Grass', 'Desc', 1000.0, 50, 'Russia', 10, 'Green')"
            in captured.out
        )
        assert lawn_grass.country == "Russia"
        assert lawn_grass.germination_period == 10
