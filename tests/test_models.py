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
            _ = (
                product + "не продукт"
            )  # Исправлено: используем _ для неиспользуемой переменной
            assert False, "Should have raised TypeError"
        except TypeError as e:
            assert "Нельзя складывать товары разных классов" in str(e)


class TestInheritance:
    """Тесты для наследования и ограничений."""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом."""
        Category.reset_counters()

    def test_smartphone_creation(self):
        """Тест создания объекта Smartphone."""
        smartphone = Smartphone(
            name="iPhone 15",
            description="Новый iPhone",
            price=100000.0,
            quantity=5,
            efficiency=3.5,
            model="15 Pro",
            memory=256,
            color="Black",
        )

        assert isinstance(smartphone, Product)
        assert isinstance(smartphone, Smartphone)
        assert smartphone.name == "iPhone 15"
        assert smartphone.price == 100000.0
        assert smartphone.efficiency == 3.5
        assert smartphone.model == "15 Pro"
        assert smartphone.memory == 256
        assert smartphone.color == "Black"

    def test_lawn_grass_creation(self):
        """Тест создания объекта LawnGrass."""
        lawn_grass = LawnGrass(
            name="Газонная трава Премиум",
            description="Качественная газонная трава",
            price=5000.0,
            quantity=100,
            country="Россия",
            germination_period=14,
            color="Зеленый",
        )

        assert isinstance(lawn_grass, Product)
        assert isinstance(lawn_grass, LawnGrass)
        assert lawn_grass.name == "Газонная трава Премиум"
        assert lawn_grass.price == 5000.0
        assert lawn_grass.country == "Россия"
        assert lawn_grass.germination_period == 14
        assert lawn_grass.color == "Зеленый"

    def test_product_addition_same_class(self):
        """Тест сложения товаров одного класса."""
        product1 = Product("Товар 1", "Описание 1", 100.0, 10)
        product2 = Product("Товар 2", "Описание 2", 200.0, 5)

        result = product1 + product2

        assert result == (100.0 * 10) + (200.0 * 5)

    def test_smartphone_addition_same_class(self):
        """Тест сложения смартфонов одного класса."""
        smartphone1 = Smartphone(
            name="Phone 1",
            description="Desc 1",
            price=50000.0,
            quantity=2,
            efficiency=3.0,
            model="A",
            memory=128,
            color="Black",
        )
        smartphone2 = Smartphone(
            name="Phone 2",
            description="Desc 2",
            price=70000.0,
            quantity=3,
            efficiency=3.5,
            model="B",
            memory=256,
            color="White",
        )

        result = smartphone1 + smartphone2

        assert result == (50000.0 * 2) + (70000.0 * 3)

    def test_lawn_grass_addition_same_class(self):
        """Тест сложения газонной травы одного класса."""
        grass1 = LawnGrass(
            name="Grass 1",
            description="Desc 1",
            price=1000.0,
            quantity=50,
            country="Russia",
            germination_period=10,
            color="Green",
        )
        grass2 = LawnGrass(
            name="Grass 2",
            description="Desc 2",
            price=1500.0,
            quantity=30,
            country="USA",
            germination_period=12,
            color="Dark Green",
        )

        result = grass1 + grass2

        assert result == (1000.0 * 50) + (1500.0 * 30)

    def test_addition_different_classes_error(self):
        """Тест ошибки при сложении товаров разных классов."""
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
        lawn_grass = LawnGrass(
            name="Grass",
            description="Desc",
            price=1000.0,
            quantity=50,
            country="Russia",
            germination_period=10,
            color="Green",
        )

        with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
            _ = (
                smartphone + lawn_grass
            )  # Исправлено: используем _ для неиспользуемой переменной

    def test_addition_product_and_smartphone_error(self):
        """Тест ошибки при сложении Product и Smartphone."""
        product = Product("Товар", "Описание", 100.0, 10)
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

        with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
            _ = (
                product + smartphone
            )  # Исправлено: используем _ для неиспользуемой переменной

    def test_addition_smartphone_and_product_error(self):
        """Тест ошибки при сложении Smartphone и Product."""
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
        product = Product("Товар", "Описание", 100.0, 10)

        with pytest.raises(TypeError, match="Нельзя складывать товары разных классов"):
            _ = (
                smartphone + product
            )  # Исправлено: используем _ для неиспользуемой переменной

    def test_add_product_valid_types(self):
        """Тест добавления различных типов продуктов в категорию."""
        category = Category("Тестовая категория", "Описание", [])

        product = Product("Товар", "Описание", 100.0, 10)
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
        lawn_grass = LawnGrass(
            name="Grass",
            description="Desc",
            price=1000.0,
            quantity=50,
            country="Russia",
            germination_period=10,
            color="Green",
        )

        category.add_product(product)
        category.add_product(smartphone)
        category.add_product(lawn_grass)

        assert len(category) == 3

    def test_add_product_invalid_type_error(self):
        """Тест ошибки при добавлении не-продукта в категорию."""
        category = Category("Тестовая категория", "Описание", [])

        with pytest.raises(
            TypeError,
            match="Можно добавлять только объекты класса Product или его наследников",
        ):
            category.add_product("не продукт")

        with pytest.raises(
            TypeError,
            match="Можно добавлять только объекты класса Product или его наследников",
        ):
            category.add_product(123)

    def test_inheritance_hierarchy(self):
        """Тест иерархии наследования."""
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
        lawn_grass = LawnGrass(
            name="Grass",
            description="Desc",
            price=1000.0,
            quantity=50,
            country="Russia",
            germination_period=10,
            color="Green",
        )

        assert isinstance(smartphone, Product)
        assert isinstance(lawn_grass, Product)
        assert issubclass(Smartphone, Product)
        assert issubclass(LawnGrass, Product)

    def test_string_representation_inherited_classes(self):
        """Тест строкового представления для классов-наследников."""
        smartphone = Smartphone(
            name="iPhone 15",
            description="Новый iPhone",
            price=100000.0,
            quantity=5,
            efficiency=3.5,
            model="15 Pro",
            memory=256,
            color="Black",
        )

        lawn_grass = LawnGrass(
            name="Газонная трава",
            description="Качественная трава",
            price=5000.0,
            quantity=100,
            country="Россия",
            germination_period=14,
            color="Зеленый",
        )

        smartphone_str = str(smartphone)
        lawn_grass_str = str(lawn_grass)

        assert "iPhone 15, 100000.0 руб. Остаток: 5 шт." in smartphone_str
        assert "Газонная трава, 5000.0 руб. Остаток: 100 шт." in lawn_grass_str
