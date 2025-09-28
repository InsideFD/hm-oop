
from src.models import Product, Category


class TestProduct:
    """Тесты для класса Product."""

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
        Category.category_count = 0
        Category.product_count = 0

    def test_category_initialization(self):
        """Тест корректной инициализации объекта Category."""
        products = [
            Product("Product 1", "Desc 1", 100.0, 5),
            Product("Product 2", "Desc 2", 200.0, 3)
        ]

        category = Category("Test Category", "Test Description", products)

        assert category.name == "Test Category"
        assert category.description == "Test Description"
        assert len(category.products) == 2
        assert isinstance(category.products[0], Product)

    def test_category_count(self):
        """Тест подсчета количества категорий."""
        assert Category.category_count == 0

        products = [Product("P1", "D1", 100.0, 1)]
        Category("Cat1", "Desc1", products)  # category1
        assert Category.category_count == 1

        Category("Cat2", "Desc2", products)  # category2
        assert Category.category_count == 2

    def test_product_count(self):
        """Тест подсчета количества товаров."""
        assert Category.product_count == 0

        products1 = [
            Product("P1", "D1", 100.0, 1),
            Product("P2", "D2", 200.0, 2)
        ]
        Category("Cat1", "Desc1", products1)  # category1
        assert Category.product_count == 2

        products2 = [Product("P3", "D3", 300.0, 3)]
        Category("Cat2", "Desc2", products2)  # category2
        assert Category.product_count == 3

    def test_category_length(self):
        """Тест метода __len__ для категории."""
        products = [
            Product("P1", "D1", 100.0, 1),
            Product("P2", "D2", 200.0, 2),
            Product("P3", "D3", 300.0, 3)
        ]
        category = Category("Test", "Desc", products)

        assert len(category) == 3

    def test_multiple_categories_product_count(self):
        """Тест корректного подсчета товаров при создании нескольких категорий."""
        # Сброс счетчиков
        Category.category_count = 0
        Category.product_count = 0

        # Создание первой категории с 2 товарами
        products1 = [
            Product("P1", "D1", 100.0, 1),
            Product("P2", "D2", 200.0, 2)
        ]
        category1 = Category("Category 1", "Description 1", products1)

        assert Category.category_count == 1
        assert Category.product_count == 2

        # Создание второй категории с 3 товарами
        products2 = [
            Product("P3", "D3", 300.0, 3),
            Product("P4", "D4", 400.0, 4),
            Product("P5", "D5", 500.0, 5)
        ]
        category2 = Category("Category 2", "Description 2", products2)

        assert Category.category_count == 2
        assert Category.product_count == 5

        # Проверка, что объекты категорий созданы корректно
        assert category1.name == "Category 1"
        assert category2.name == "Category 2"
        assert len(category1.products) == 2
        assert len(category2.products) == 3
