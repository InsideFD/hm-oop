from src.models import Category, CategoryIterator, Product


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
        assert product.price == 1000.0  # Используем геттер
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
        assert len(category) == 2  # Используем __len__
        # Проверяем через геттер
        products_str = category.products
        assert "Product 1" in products_str
        assert "Product 2" in products_str

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


class TestNewFeatures:
    """Тесты для новой функциональности."""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом."""
        Category.reset_counters()

    def test_private_products_attribute(self):
        """Тест приватного атрибута продуктов."""
        product = Product("Test", "Desc", 100.0, 5)
        category = Category("Test Category", "Description", [product])

        assert hasattr(category, "_products")
        assert len(category._products) == 1

    def test_add_product_method(self):
        """Тест метода add_product."""
        category = Category("Test Category", "Description", [])
        product = Product("Test Product", "Desc", 100.0, 5)

        initial_count = Category.product_count

        category.add_product(product)

        assert len(category) == 1
        assert Category.product_count == initial_count + 1

    def test_add_product_invalid_type(self):
        """Тест добавления неверного типа в add_product."""
        category = Category("Test Category", "Description", [])

        try:
            category.add_product("not a product")
            assert False, "Should have raised TypeError"
        except TypeError:
            assert True

    def test_products_getter(self):
        """Тест геттера products."""
        product1 = Product("Product 1", "Desc 1", 100.0, 5)
        product2 = Product("Product 2", "Desc 2", 200.0, 3)

        category = Category("Test Category", "Description", [product1, product2])

        products_string = category.products

        assert "Product 1, 100.0 руб. Остаток: 5 шт." in products_string
        assert "Product 2, 200.0 руб. Остаток: 3 шт." in products_string
        assert isinstance(products_string, str)

    def test_class_method_new_product(self):
        """Тест класс-метода new_product."""
        product_data = {
            "name": "New Product",
            "description": "New Description",
            "price": 150.0,
            "quantity": 10,
        }

        product = Product.new_product(product_data)

        assert isinstance(product, Product)
        assert product.name == "New Product"
        assert product.description == "New Description"
        assert product.price == 150.0
        assert product.quantity == 10

    def test_private_price_attribute(self):
        """Тест приватного атрибута цены с двойным подчеркиванием."""
        product = Product("Test", "Desc", 100.0, 5)

        assert hasattr(product, "_Product__price")
        assert product._Product__price == 100.0

        try:
            _ = product.__price
            assert False, "Should have raised AttributeError"
        except AttributeError:
            assert True

    def test_price_getter(self):
        """Тест геттера цены."""
        product = Product("Test", "Desc", 100.0, 5)

        assert product.price == 100.0

    def test_price_setter_positive(self):
        """Тест сеттера цены с положительным значением."""
        product = Product("Test", "Desc", 100.0, 5)

        product.price = 200.0

        assert product.price == 200.0
        assert product._Product__price == 200.0

        def test_price_getter_setter():
            """Тест что геттер и сеттер работают корректно с приватным атрибутом."""
            product = Product("Test", "Description", 100.0, 5)

            # Проверяем геттер
            assert product.price == 100.0

            # Проверяем сеттер с корректным значением
            product.price = 150.0
            assert product.price == 150.0
            assert product._Product__price == 150.0

            # Проверяем сеттер с некорректным значением
            import io
            import sys

            captured_output = io.StringIO()
            sys.stdout = captured_output

            product.price = -50.0  # Попытка установить отрицательную цену

            sys.stdout = sys.__stdout__

            # Цена не должна измениться
            assert product.price == 150.0
            assert (
                "Цена не должна быть нулевая или отрицательная"
                in captured_output.getvalue()
            )

    def test_price_setter_negative(self):
        """Тест сеттера цены с отрицательным значением."""
        product = Product("Test", "Desc", 100.0, 5)

        import io
        import sys

        captured_output = io.StringIO()
        sys.stdout = captured_output

        product.price = -50.0

        sys.stdout = sys.__stdout__

        assert product.price == 100.0
        assert product._Product__price == 100.0
        assert (
            "Цена не должна быть нулевая или отрицательная"
            in captured_output.getvalue()
        )

    def test_price_setter_zero(self):
        """Тест сеттера цены с нулевым значением."""
        product = Product("Test", "Desc", 100.0, 5)

        import io
        import sys

        captured_output = io.StringIO()
        sys.stdout = captured_output

        product.price = 0.0

        sys.stdout = sys.__stdout__

        assert product.price == 100.0
        assert (
            "Цена не должна быть нулевая или отрицательная"
            in captured_output.getvalue()
        )

    def test_product_string_representation(self):
        """Тест строкового представления продукта."""
        product = Product("Test Product", "Description", 150.0, 8)

        product_str = str(product)

        assert product_str == "Test Product, 150.0 руб. Остаток: 8 шт."

    def test_category_counters_with_add_product(self):
        """Тест счетчиков при использовании add_product."""
        initial_category_count = Category.category_count
        initial_product_count = Category.product_count

        category = Category("Test Category", "Description", [])
        product1 = Product("P1", "D1", 100.0, 1)
        product2 = Product("P2", "D2", 200.0, 2)

        category.add_product(product1)
        category.add_product(product2)

        assert Category.category_count == initial_category_count + 1
        assert Category.product_count == initial_product_count + 2


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
        expected = "Тестовая категория, количество продуктов: 8 шт."  # 5 + 3 = 8

        assert result == expected

    def test_category_str_empty(self):
        """Тест строкового представления пустой категории."""
        category = Category("Пустая категория", "Описание", [])

        result = str(category)
        expected = "Пустая категория, количество продуктов: 0 шт."

        assert result == expected

    def test_product_addition(self):
        """Тест сложения двух продуктов."""
        product1 = Product("Товар 1", "Описание 1", 100.0, 10)  # 100 * 10 = 1000
        product2 = Product("Товар 2", "Описание 2", 200.0, 5)  # 200 * 5 = 1000

        result = product1 + product2

        assert result == 2000.0  # 1000 + 1000 = 2000

    def test_product_addition_different_prices(self):
        """Тест сложения продуктов с разными ценами."""
        product1 = Product("Товар 1", "Описание 1", 50.0, 4)  # 50 * 4 = 200
        product2 = Product("Товар 2", "Описание 2", 150.0, 2)  # 150 * 2 = 300

        result = product1 + product2

        assert result == 500.0  # 200 + 300 = 500

    def test_product_addition_invalid_type(self):
        """Тест сложения продукта с неверным типом."""
        product = Product("Товар", "Описание", 100.0, 5)

        try:
            result = product + "не продукт"
            assert False, "Should have raised TypeError"
        except TypeError as e:
            assert "Можно складывать только объекты класса Product" in str(e)

    def test_category_iterator(self):
        """Тест итератора категории."""
        products = [
            Product("Товар 1", "Описание 1", 100.0, 5),
            Product("Товар 2", "Описание 2", 200.0, 3),
            Product("Товар 3", "Описание 3", 300.0, 2),
        ]
        category = Category("Тестовая категория", "Описание", products)

        # Тестируем итерацию
        iterated_products = []
        for product in category:
            iterated_products.append(product)

        assert len(iterated_products) == 3
        assert iterated_products[0].name == "Товар 1"
        assert iterated_products[1].name == "Товар 2"
        assert iterated_products[2].name == "Товар 3"

    def test_category_iterator_empty(self):
        """Тест итератора пустой категории."""
        category = Category("Пустая категория", "Описание", [])

        iterated_products = list(category)

        assert len(iterated_products) == 0

    def test_category_iterator_direct(self):
        """Тест прямого использования итератора."""
        products = [
            Product("Товар 1", "Описание 1", 100.0, 5),
            Product("Товар 2", "Описание 2", 200.0, 3),
        ]
        iterator = CategoryIterator(products)

        product1 = next(iterator)
        product2 = next(iterator)

        assert product1.name == "Товар 1"
        assert product2.name == "Товар 2"

        # Должно вызвать StopIteration
        try:
            next(iterator)
            assert False, "Should have raised StopIteration"
        except StopIteration:
            assert True

    def test_products_getter_uses_str(self):
        """Тест что геттер products использует __str__ метод."""
        product = Product("Тестовый товар", "Описание", 150.0, 10)
        category = Category("Тестовая категория", "Описание", [product])

        products_string = category.products

        assert "Тестовый товар, 150.0 руб. Остаток: 10 шт." in products_string
