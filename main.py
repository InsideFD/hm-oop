from src.models import Product, Smartphone, LawnGrass, Category, Order


def demonstrate_abstract_classes_and_mixins():
    """Демонстрация абстрактных классов и миксинов."""
    print("=== ДЕМОНСТРАЦИЯ АБСТРАКТНЫХ КЛАССОВ И МИКСИНОВ ===")

    print("\n1. Создание продуктов (должны выводиться сообщения о создании):")

    # Создание обычного продукта
    product = Product("Обычный товар", "Просто товар", 500.0, 20)
    print(f"   Создан: {product}")

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
    print(f"   Создан: {smartphone}")

    lawn_grass = LawnGrass(
        name="Газонная трава 'Изумруд'",
        description="Премиальная газонная трава",
        price=4500.0,
        quantity=150,
        country="Германия",
        germination_period=12,
        color="Ярко-зеленый"
    )
    print(f"   Создан: {lawn_grass}")

    print(f"\n2. Проверка наследования:")
    print(f"   Product является BaseProduct: {isinstance(product, Product)}")
    print(f"   Smartphone является Product: {isinstance(smartphone, Product)}")
    print(f"   LawnGrass является Product: {isinstance(lawn_grass, Product)}")
    print(f"   Все являются BaseProduct: {isinstance(product, type(product))}")

    print(f"\n3. Создание заказов:")

    order1 = Order(product, 5)
    print(f"   Заказ 1: {order1}")

    order2 = Order(smartphone, 2)
    print(f"   Заказ 2: {order2}")

    order3 = Order(lawn_grass, 25)
    print(f"   Заказ 3: {order3}")

    total_orders = order1.total_price + order2.total_price + order3.total_price
    print(f"\n4. Итоговая стоимость всех заказов: {total_orders} руб.")


def demonstrate_previous_functionality():
    """Демонстрация что предыдущая функциональность работает."""
    print("\n=== ПРОВЕРКА ПРЕДЫДУЩЕЙ ФУНКЦИОНАЛЬНОСТИ ===")

    products = [
        Product("Товар 1", "Описание 1", 100.0, 10),
        Product("Товар 2", "Описание 2", 200.0, 5),
    ]
    category = Category("Тестовая категория", "Описание", products)

    print(f"\nКатегория: {category}")
    print("Товары в категории:")
    for product in category:
        print(f"  - {product}")

    # Проверка сложения
    product1 = Product("Товар A", "Описание", 50.0, 4)
    product2 = Product("Товар B", "Описание", 150.0, 2)
    total = product1 + product2
    print(f"\nСумма товаров на складе: {total} руб.")


if __name__ == "__main__":
    demonstrate_abstract_classes_and_mixins()
    demonstrate_previous_functionality()
