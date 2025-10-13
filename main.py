from src.models import Product, Smartphone, LawnGrass, Category


def demonstrate_inheritance():
    """Демонстрация наследования и новых классов."""
    print("=== ДЕМОНСТРАЦИЯ НАСЛЕДОВАНИЯ ===")

    # Создание обычного продукта
    product = Product("Обычный товар", "Просто товар", 500.0, 20)
    print(f"\n1. Обычный продукт: {product}")

    # Создание смартфона
    smartphone = Smartphone(
        name="Samsung Galaxy S24",
        description="Флагманский смартфон",
        price=120000.0,
        quantity=8,
        efficiency=4.2,
        model="S24 Ultra",
        memory=512,
        color="Титановый серый"
    )
    print(f"\n2. Смартфон: {smartphone}")
    print(f"   Производительность: {smartphone.efficiency} ГГц")
    print(f"   Модель: {smartphone.model}")
    print(f"   Память: {smartphone.memory} ГБ")
    print(f"   Цвет: {smartphone.color}")

    # Создание газонной травы
    lawn_grass = LawnGrass(
        name="Газонная трава 'Изумруд'",
        description="Премиальная газонная трава",
        price=4500.0,
        quantity=150,
        country="Германия",
        germination_period=12,
        color="Ярко-зеленый"
    )
    print(f"\n3. Газонная трава: {lawn_grass}")
    print(f"   Страна: {lawn_grass.country}")
    print(f"   Срок прорастания: {lawn_grass.germination_period} дней")
    print(f"   Цвет: {lawn_grass.color}")

    # Демонстрация сложения одинаковых классов
    print(f"\n4. Сложение товаров одинаковых классов:")

    smartphone2 = Smartphone(
        name="iPhone 15 Pro", description="Apple смартфон", price=130000.0, quantity=5,
        efficiency=3.8, model="15 Pro", memory=256, color="Синий"
    )

    total_smartphones = smartphone + smartphone2
    print(f"   Общая стоимость смартфонов на складе: {total_smartphones} руб.")

    # Демонстрация ошибки при сложении разных классов
    print(f"\n5. Попытка сложения разных классов:")
    try:
        invalid_sum = smartphone + lawn_grass
        print(f"   Результат: {invalid_sum}")  # Эта строка не выполнится
    except TypeError as e:
        print(f"   Ошибка: {e}")

    # Демонстрация работы с категориями
    print(f"\n6. Работа с категориями и разными типами продуктов:")

    electronics_category = Category("Электроника", "Техника и гаджеты", [])

    # Добавляем разные типы продуктов
    electronics_category.add_product(smartphone)
    electronics_category.add_product(smartphone2)

    garden_category = Category("Сад и огород", "Товары для сада", [])
    garden_category.add_product(lawn_grass)

    print(f"   Категория '{electronics_category.name}': {electronics_category}")
    print(f"   Категория '{garden_category.name}': {garden_category}")

    # Демонстрация ошибки при добавлении не-продукта
    print(f"\n7. Попытка добавления не-продукта в категорию:")
    try:
        electronics_category.add_product("Это не продукт")
        print("   Успешно добавлено")  # Эта строка не выполнится
    except TypeError as e:
        print(f"   Ошибка: {e}")


def demonstrate_previous_functionality():
    """Демонстрация что предыдущая функциональность работает."""
    print("\n=== ПРОВЕРКА ПРЕДЫДУЩЕЙ ФУНКЦИОНАЛЬНОСТИ ===")

    # Проверка работы итератора
    products = [
        Product("Товар 1", "Описание 1", 100.0, 10),
        Product("Товар 2", "Описание 2", 200.0, 5),
    ]
    category = Category("Тестовая категория", "Описание", products)

    print("\nИтерация по категории:")
    for i, product in enumerate(category, 1):
        print(f"  {i}. {product}")

    # Проверка работы с ценой
    print(f"\nРабота с ценой:")
    product = Product("Тестовый товар", "Описание", 1000.0, 2)
    print(f"  Исходная цена: {product.price}")
    product.price = 1500.0
    print(f"  Новая цена: {product.price}")


if __name__ == "__main__":
    demonstrate_inheritance()
    demonstrate_previous_functionality()