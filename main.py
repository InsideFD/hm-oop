from src.models import Product, Category
from src.utils import load_products_from_json


def demonstrate_classes():
    """Демонстрация работы основных классов."""
    # Создание товаров
    product1 = Product(
        "Samsung Galaxy S23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5
    )
    product2 = Product("Iphone 15", "512GB, Gray space", 210000.0, 8)
    product3 = Product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)

    # Вывод информации о товарах
    print("Информация о товарах:")
    print(f"{product1.name} - {product1.price} руб. - {product1.quantity} шт.")
    print(f"{product2.name} - {product2.price} руб. - {product2.quantity} шт.")
    print(f"{product3.name} - {product3.price} руб. - {product3.quantity} шт.")
    print()

    # Создание категории
    category1 = Category(
        "Смартфоны",
        "Смартфоны, как средство не только коммуникации, но и получения дополнительных функций для удобства жизни",
        [product1, product2, product3],
    )

    # Проверка атрибутов категории
    print("Информация о категории:")
    print(f"Название: {category1.name}")
    print(f"Описание: {category1.description}")
    print(f"Количество товаров: {len(category1.products)}")
    print(f"Всего категорий: {Category.category_count}")
    print(f"Всего товаров: {Category.product_count}")
    print()

    # Создание второй категории
    product4 = Product('55" QLED 4K', "Фоновая подсветка", 123000.0, 7)
    category2 = Category(
        "Телевизоры",
        "Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",
        [product4],
    )

    print("Информация о второй категории:")
    print(f"Название: {category2.name}")
    print(f"Описание: {category2.description}")
    print(f"Количество товаров: {len(category2.products)}")
    print()

    # Общая статистика
    print("Общая статистика:")
    print(f"Всего категорий в системе: {Category.category_count}")
    print(f"Всего товаров в системе: {Category.product_count}")
    print()


def demonstrate_json_loading():
    """Демонстрация загрузки данных из JSON."""
    print("Загрузка данных из JSON...")
    categories_from_json = load_products_from_json("data/products.json")

    if categories_from_json:
        print(f"Загружено категорий из JSON: {len(categories_from_json)}")
        for category in categories_from_json:
            print(f"- {category.name}: {len(category)} товаров")
            for product in category.products:
                print(f"  * {product.name} - {product.price} руб.")
    else:
        print("Не удалось загрузить данные из JSON файла")
    print()


if __name__ == "__main__":
    demonstrate_classes()
    demonstrate_json_loading()