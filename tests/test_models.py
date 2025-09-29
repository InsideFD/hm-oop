from src.models import Category, Product


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

    def test_product_string_representation(self):
        """Тест строкового представления продукта."""
        product = Product("Test Product", "Test Desc", 100.0, 5)
        assert "Test Product" in product.name
        assert product.price == 100.0


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
            Product("Product 2", "Desc 2", 200.0, 3),
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
        Category("Cat1", "Desc1", products)
        assert Category.category_count == 1

        Category("Cat2", "Desc2", products)
        assert Category.category_count == 2

    def test_product_count(self):
        """Тест подсчета количества товаров."""
        assert Category.product_count == 0

        products1 = [
            Product("P1", "D1", 100.0, 1),
            Product("P2", "D2", 200.0, 2),
        ]
        Category("Cat1", "Desc1", products1)
        assert Category.product_count == 2

        products2 = [Product("P3", "D3", 300.0, 3)]
        Category("Cat2", "Desc2", products2)
        assert Category.product_count == 3

    def test_category_length(self):
        """Тест метода __len__ для категории."""
        products = [
            Product("P1", "D1", 100.0, 1),
            Product("P2", "D2", 200.0, 2),
            Product("P3", "D3", 300.0, 3),
        ]
        category = Category("Test", "Desc", products)

        assert len(category) == 3

    def test_empty_category(self):
        """Тест создания категории без товаров."""
        category = Category("Empty Category", "No products", [])

        assert category.name == "Empty Category"
        assert len(category.products) == 0
        assert Category.category_count == 1
        assert Category.product_count == 0

    def test_category_with_single_product(self):
        """Тест категории с одним товаром."""
        product = Product("Single Product", "Only one", 50.0, 1)
        category = Category("Single Category", "One product", [product])

        assert len(category) == 1
        assert Category.product_count == 1
