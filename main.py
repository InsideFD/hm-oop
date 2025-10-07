from src.models import Product, Category
from src.utils import load_products_from_json


def demonstrate_magic_methods():
    """Демонстрация магических методов."""
    print("=== ДЕМОНСТРАЦИЯ МАГИЧЕСКИХ МЕТОДОВ ===")

    # Создание товаров
    product1 = Product("Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Демонстрация __str__ для продуктов
    print("\n1. Строковое представление продуктов:")
    print(product1)
    print(product2)
    print(product3)

    # Создание категории
    category = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    # Демонстрация __str__ для категории
    print(f"\n2. Строковое представление категории:")
    print(category)

    # Демонстрация сложения продуктов
    print(f"\n3. Сложение продуктов (общая стоимость товаров на складе):")
    total_value = product1 + product2
    print(f"Стоимость {product1.name} и {product2.name} на складе: {total_value} руб.")

    total_all = product1 + product2 + product3
    print(f"Общая стоимость всех трех товаров на складе: {total_all} руб.")

    # Демонстрация итератора категории
    print(f"\n4. Итерация по товарам категории:")
    for i, product in enumerate(category, 1):
        print(f"{i}. {product}")

    # Демонстрация с пустой категорией
    empty_category = Category("Пустая категория", "Нет товаров", [])
    print(f"\n5. Пустая категория:")
    print(empty_category)
    print("Товары в пустой категории:")
    for product in empty_category:
        print(product)  # Этот блок не выполнится
    print("(товаров нет)")


def demonstrate_previous_functionality():
    """Демонстрация предыдущей функциональности."""
    print("\n=== ДЕМОНСТРАЦИЯ ПРЕДЫДУЩЕЙ ФУНКЦИОНАЛЬНОСТИ ===")

    # Проверка работы геттера products
    product1 = Product("Тестовый товар 1", "Описание 1", 1000.0, 2)
    product2 = Product("Тестовый товар 2", "Описание 2", 2000.0, 3)

    category = Category("Тестовая категория", "Описание", [product1, product2])

    print("\nГеттер products:")
    print(category.products)

    # Проверка работы с ценой
    print(f"\nРабота с ценой:")
    print(f"Исходная цена: {product1.price}")
    product1.price = 1500.0
    print(f"Новая цена: {product1.price}")
    print("Попытка установить отрицательную цену:")
    product1.price = -500


def demonstrate_json_loading():
    """Демонстрация загрузки данных из JSON."""
    print("\n=== ЗАГРУЗКА ИЗ JSON ===")
    categories_from_json = load_products_from_json("data/products.json")

    if categories_from_json:
        print(f"Загружено категорий из JSON: {len(categories_from_json)}")
        for category in categories_from_json:
            print(f"\n{category}")  # Используем __str__
            print("Товары:")
            for product in category:
                print(f"  - {product}")  # Используем __str__
    else:
        print("Не удалось загрузить данные из JSON файла")


if __name__ == "__main__":
    demonstrate_magic_methods()
    demonstrate_previous_functionality()
    demonstrate_json_loading()