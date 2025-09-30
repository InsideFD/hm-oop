from src.models import Product, Category
from src.utils import load_products_from_json


def demonstrate_basic_functionality():
    """Демонстрация базовой функциональности."""
    print("=== ДЕМОНСТРАЦИЯ БАЗОВОЙ ФУНКЦИОНАЛЬНОСТИ ===")

    # Создание товаров
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Вывод информации о товарах
    print("\n1. Информация о товарах:")
    print(product1)
    print(product2)
    print(product3)

    # Создание категории
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    # Проверка атрибутов категории
    print(f"\n2. Название категории: {category1.name}")
    print(f"Описание категории: {category1.description}")
    print(f"Количество товаров в категории: {len(category1)}")
    print(f"Всего категорий в системе: {Category.category_count}")
    print(f"Всего товаров в системе: {Category.product_count}")

    # Демонстрация геттера products
    print("\n3. Список товаров в категории (через геттер):")
    print(category1.products)

    # Создание второй категории
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print(f"\n4. Вторая категория: {category2.name}")
    print(f"Количество товаров: {len(category2)}")

    # Общая статистика
    print("\n5. Общая статистика:")
    print(f"Всего категорий в системе: {Category.category_count}")
    print(f"Всего товаров в системе: {Category.product_count}")


def demonstrate_new_features():
    """Демонстрация новой функциональности."""
    print("\n=== ДЕМОНСТРАЦИЯ НОВОЙ ФУНКЦИОНАЛЬНОСТИ ===")

    print("\n1. Создание продукта через класс-метод:")
    product_data = {
        "name": "Huawei P60 Pro",
        "description": "256GB, Черный, камера Leica",
        "price": 120000.0,
        "quantity": 6
    }
    new_product = Product.new_product(product_data)
    print(f"Создан продукт: {new_product}")

    print("\n2. Добавление продукта в категорию:")
    category = Category("Тестовые товары", "Категория для тестирования", [])
    print(f"Товаров в категории до добавления: {len(category)}")

    category.add_product(new_product)
    print(f"Товаров в категории после добавления: {len(category)}")
    print("Список товаров:")
    print(category.products)

    print("\n3. Работа с приватным атрибутом цены:")
    test_product = Product("Тестовый товар", "Описание", 1000.0, 10)
    print(f"Исходная цена: {test_product.price} руб.")

    print("Попытка установить цену -500 руб.:")
    test_product.price = -500

    test_product.price = 1500.0
    print(f"Новая цена: {test_product.price} руб.")

    # Проверка счетчиков после добавления товаров
    print(f"\n4. Итоговые счетчики:")
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")


def demonstrate_json_loading():
    """Демонстрация загрузки данных из JSON."""
    print("\n=== ЗАГРУЗКА ИЗ JSON ===")
    categories_from_json = load_products_from_json("data/products.json")

    if categories_from_json:
        print(f"Загружено категорий из JSON: {len(categories_from_json)}")
        for category in categories_from_json:
            print(f"\n{category.name}:")
            print(category.products)
    else:
        print("Не удалось загрузить данные из JSON файла")


if __name__ == "__main__":
    demonstrate_basic_functionality()
    demonstrate_new_features()
    demonstrate_json_loading()