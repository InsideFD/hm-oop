import pytest

from src.models import Category, LawnGrass, Product, Smartphone


class TestProduct:
    """Тесты для класса Product."""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом."""
        Category.reset_counters()

    def test_product_initialization(self):
        """Тест корректной инициализации объекта Product."""
        product = Product("Test Product", "Test Description", 1000.0, 10)

        assert product.name == "Test Product"
        assert product.description == "Test Description"
        assert product.price == 1000.0
        assert product.quantity == 10

    def test_product_attributes_types(self):
        """Тест типов данных атрибутов Product."""
        product = Product("Test", "Desc", 500.0, 5)

        assert isinstance(product.name, str)
        assert isinstance(product.description, str)
        assert isinstance(product.price, float)
        assert isinstance(product.quantity, int)


class TestCategory:
    """Тесты для класса Category."""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом."""
        Category.reset_counters()

    def test_category_initialization(self):
        """Тест корректной инициализации объекта Category."""
        products = [
            Product("Product 1", "Desc 1", 100.0, 5),
            Product("Product 2", "Desc 2", 200.0, 3),
        ]

        category = Category("Test Category", "Test Description", products)

        assert category.name == "Test Category"
        assert category.description == "Test Description"
        assert len(category) == 2
        products_str = category.products
        assert "Product 1" in products_str
        assert "Product 2" in products_str


class TestMagicMethods:
    """Тесты для магических методов."""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом."""
        Category.reset_counters()

    def test_product_str_method(self):
        """Тест строкового представления продукта."""
        product = Product("Тестовый товар", "Описание", 150.0, 10)

        result = str(product)
        expected = "Тестовый товар, 150.0 руб. Остаток: 10 шт."

        assert result == expected

    def test_category_str_method(self):
        """Тест строкового представления категории."""
        products = [
            Product("Товар 1", "Описание 1", 100.0, 5),
            Product("Товар 2", "Описание 2", 200.0, 3),
        ]
        category = Category("Тестовая категория", "Описание", products)

        result = str(category)
        expected = "Тестовая категория, количество продуктов: 8 шт."

        assert result == expected

    def test_category_str_empty(self):
        """Тест строкового представления пустой категории."""
        category = Category("Пустая категория", "Описание", [])

        result = str(category)
        expected = "Пустая категория, количество продуктов: 0 шт."

        assert result == expected

    def test_product_addition(self):
        """Тест сложения двух продуктов."""
        product1 = Product("Товар 1", "Описание 1", 100.0, 10)
        product2 = Product("Товар 2", "Описание 2", 200.0, 5)

        result = product1 + product2

        assert result == 2000.0

    def test_product_addition_different_prices(self):
        """Тест сложения продуктов с разными ценами."""
        product1 = Product("Товар 1", "Описание 1", 50.0, 4)
        product2 = Product("Товар 2", "Описание 2", 150.0, 2)

        result = product1 + product2

        assert result == 500.0

    def test_product_addition_invalid_type(self):
        """Тест сложения продукта с неверным типом."""
        product = Product("Товар", "Описание", 100.0, 5)

        try:
            _ = product + "не продукт"
            assert False, "Should have raised TypeError"
        except TypeError as e:
            assert "Нельзя складывать товары разных классов" in str(e)


class TestInheritance:
    """Тесты для наследования и ограничений."""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом."""
        Category.reset_counters()

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
        assert lawn_grass.country == "Russia"
        assert lawn_grass.germination_period == 10
        assert lawn_grass.color == "Green"

    def test_logging_mixin_functionality(self, capsys):
        """Тест функциональности миксина логирования."""
        _ = Product("Test Product", "Description", 100.0, 5)

        captured = capsys.readouterr()
        assert (
            "Создан объект Product с параметрами: Product('Test Product', 'Description', 100.0, 5)"
            in captured.out
        )

    def test_logging_mixin_in_smartphone(self, capsys):
        """Тест что миксин работает в Smartphone."""
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

    def test_logging_mixin_in_lawn_grass(self, capsys):
        """Тест что миксин работает в LawnGrass."""
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


class TestExceptions:
    """Тесты для обработки исключений."""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом."""
        Category.reset_counters()

    def test_product_zero_quantity_raises_value_error(self):
        """Тест что создание продукта с нулевым количеством вызывает ValueError."""
        with pytest.raises(
            ValueError, match="Товар с нулевым количеством не может быть добавлен"
        ):
            Product("Test Product", "Description", 100.0, 0)

    def test_smartphone_zero_quantity_raises_value_error(self):
        """Тест что создание смартфона с нулевым количеством вызывает ValueError."""
        with pytest.raises(
            ValueError, match="Товар с нулевым количеством не может быть добавлен"
        ):
            Smartphone(
                name="Phone",
                description="Desc",
                price=50000.0,
                quantity=0,
                efficiency=3.0,
                model="A",
                memory=128,
                color="Black",
            )

    def test_lawn_grass_zero_quantity_raises_value_error(self):
        """Тест что создание газонной травы с нулевым количеством вызывает ValueError."""
        with pytest.raises(
            ValueError, match="Товар с нулевым количеством не может быть добавлен"
        ):
            LawnGrass(
                name="Grass",
                description="Desc",
                price=1000.0,
                quantity=0,
                country="Russia",
                germination_period=10,
                color="Green",
            )

    def test_product_positive_quantity_creates_successfully(self):
        """Тест что создание продукта с положительным количеством работает."""
        product = Product("Test Product", "Description", 100.0, 5)
        assert product.quantity == 5

    def test_category_average_price_with_products(self):
        """Тест расчета средней цены для категории с товарами."""
        products = [
            Product("Product 1", "Desc 1", 100.0, 5),
            Product("Product 2", "Desc 2", 200.0, 3),
            Product("Product 3", "Desc 3", 300.0, 2),
        ]
        category = Category("Test Category", "Description", products)

        average_price = category.average_price()
        expected_average = (100.0 + 200.0 + 300.0) / 3  # 600 / 3 = 200
        assert average_price == expected_average

    def test_category_average_price_single_product(self):
        """Тест расчета средней цены для категории с одним товаром."""
        product = Product("Single Product", "Description", 150.0, 1)
        category = Category("Test Category", "Description", [product])

        average_price = category.average_price()
        assert average_price == 150.0

    def test_category_average_price_empty_category(self):
        """Тест расчета средней цены для пустой категории."""
        category = Category("Empty Category", "Description", [])

        average_price = category.average_price()
        assert average_price == 0

    def test_category_average_price_with_smartphones(self):
        """Тест расчета средней цены для категории со смартфонами."""
        smartphones = [
            Smartphone(
                name="Phone 1",
                description="Desc 1",
                price=50000.0,
                quantity=2,
                efficiency=3.0,
                model="A",
                memory=128,
                color="Black",
            ),
            Smartphone(
                name="Phone 2",
                description="Desc 2",
                price=70000.0,
                quantity=3,
                efficiency=3.5,
                model="B",
                memory=256,
                color="White",
            ),
        ]
        category = Category("Smartphones Category", "Description", smartphones)

        average_price = category.average_price()
        expected_average = (50000.0 + 70000.0) / 2  # 120000 / 2 = 60000
        assert average_price == expected_average

    def test_category_average_price_with_lawn_grass(self):
        """Тест расчета средней цены для категории с газонной травой."""
        lawn_grasses = [
            LawnGrass(
                name="Grass 1",
                description="Desc 1",
                price=1000.0,
                quantity=50,
                country="Russia",
                germination_period=10,
                color="Green",
            ),
            LawnGrass(
                name="Grass 2",
                description="Desc 2",
                price=1500.0,
                quantity=30,
                country="USA",
                germination_period=12,
                color="Dark Green",
            ),
        ]
        category = Category("Lawn Grass Category", "Description", lawn_grasses)

        average_price = category.average_price()
        expected_average = (1000.0 + 1500.0) / 2  # 2500 / 2 = 1250
        assert average_price == expected_average

    def test_category_average_price_after_adding_products(self):
        """Тест расчета средней цены после добавления товаров."""
        category = Category("Test Category", "Description", [])

        assert category.average_price() == 0

        product1 = Product("Product 1", "Desc 1", 100.0, 5)
        product2 = Product("Product 2", "Desc 2", 200.0, 3)

        category.add_product(product1)
        category.add_product(product2)

        average_price = category.average_price()
        expected_average = (100.0 + 200.0) / 2  # 300 / 2 = 150
        assert average_price == expected_average

    def test_product_new_product_with_zero_quantity(self):
        """Тест что класс-метод new_product тоже проверяет нулевое количество."""
        product_data = {
            "name": "New Product",
            "description": "New Description",
            "price": 150.0,
            "quantity": 0,
        }

        with pytest.raises(
            ValueError, match="Товар с нулевым количеством не может быть добавлен"
        ):
            Product.new_product(product_data)

    def test_product_new_product_with_positive_quantity(self):
        """Тест класс-метод new_product работает с положительным количеством."""
        product_data = {
            "name": "New Product",
            "description": "New Description",
            "price": 150.0,
            "quantity": 10,
        }

        product = Product.new_product(product_data)
        assert product.quantity == 10
        assert product.name == "New Product"
