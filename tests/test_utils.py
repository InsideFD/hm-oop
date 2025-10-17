import json
import os
import tempfile

from src.models import Category, Product
from src.utils import load_products_from_json


class TestJsonUtils:
    """Тесты для JSON утилит."""

    def setup_method(self):
        """Сброс счетчиков перед каждым тестом."""
        Category.reset_counters()

    def test_load_products_from_json_valid_file(self):
        """Тест загрузки данных из корректного JSON файла."""
        # Создаем временный JSON файл
        test_data = [
            {
                "name": "Ноутбуки",
                "description": "Мощные ноутбуки для работы и игр",
                "products": [
                    {
                        "name": "MacBook Pro 16",
                        "description": "M2 Pro, 16GB, 1TB SSD",
                        "price": 250000.0,
                        "quantity": 3,
                    },
                    {
                        "name": "Dell XPS 15",
                        "description": "Intel i7, 16GB, 512GB SSD",
                        "price": 150000.0,
                        "quantity": 5,
                    },
                ],
            }
        ]

        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            json.dump(test_data, f, ensure_ascii=False)
            temp_file_path = f.name

        try:
            # Загружаем данные из файла
            categories = load_products_from_json(temp_file_path)

            # Проверяем результат
            assert len(categories) == 1
            assert isinstance(categories[0], Category)
            assert categories[0].name == "Ноутбуки"
            assert len(categories[0]) == 2  # Используем __len__
            assert isinstance(categories[0]._products[0], Product)
            assert categories[0]._products[0].name == "MacBook Pro 16"
            assert categories[0]._products[0].price == 250000.0
            assert categories[0]._products[1].name == "Dell XPS 15"
            assert categories[0]._products[1].quantity == 5

        finally:
            # Удаляем временный файл
            if os.path.exists(temp_file_path):
                os.unlink(temp_file_path)

    def test_load_products_from_json_file_not_found(self):
        """Тест загрузки при отсутствии файла."""
        categories = load_products_from_json("nonexistent_file.json")
        assert categories == []

    def test_load_products_from_json_invalid_json(self):
        """Тест загрузки из некорректного JSON файла."""
        # Создаем временный файл с некорректным JSON
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            f.write("invalid json content")
            temp_file_path = f.name

        try:
            categories = load_products_from_json(temp_file_path)
            assert categories == []
        finally:
            if os.path.exists(temp_file_path):
                os.unlink(temp_file_path)

    def test_load_products_from_json_empty_file(self):
        """Тест загрузки из пустого JSON файла."""
        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            json.dump([], f, ensure_ascii=False)
            temp_file_path = f.name

        try:
            categories = load_products_from_json(temp_file_path)
            assert categories == []
        finally:
            if os.path.exists(temp_file_path):
                os.unlink(temp_file_path)

    def test_load_products_from_json_multiple_categories(self):
        """Тест загрузки нескольких категорий из JSON."""
        test_data = [
            {
                "name": "Категория 1",
                "description": "Описание 1",
                "products": [
                    {
                        "name": "Товар 1",
                        "description": "Описание товара 1",
                        "price": 100.0,
                        "quantity": 1,
                    }
                ],
            },
            {
                "name": "Категория 2",
                "description": "Описание 2",
                "products": [
                    {
                        "name": "Товар 2",
                        "description": "Описание товара 2",
                        "price": 200.0,
                        "quantity": 2,
                    },
                    {
                        "name": "Товар 3",
                        "description": "Описание товара 3",
                        "price": 300.0,
                        "quantity": 3,
                    },
                ],
            },
        ]

        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            json.dump(test_data, f, ensure_ascii=False)
            temp_file_path = f.name

        try:
            categories = load_products_from_json(temp_file_path)

            assert len(categories) == 2
            assert categories[0].name == "Категория 1"
            assert len(categories[0]) == 1  # Используем __len__
            assert categories[1].name == "Категория 2"
            assert len(categories[1]) == 2  # Используем __len__

        finally:
            if os.path.exists(temp_file_path):
                os.unlink(temp_file_path)

    def test_load_products_from_json_with_special_characters(self):
        """Тест загрузки JSON с специальными символами."""
        test_data = [
            {
                "name": "Тестовая категория",
                "description": "Описание с спецсимволами: ©®™",
                "products": [
                    {
                        "name": 'Товар с цитатой "test"',
                        "description": "Описание 'одинарные' кавычки",
                        "price": 100.0,
                        "quantity": 1,
                    }
                ],
            }
        ]

        with tempfile.NamedTemporaryFile(
            mode="w", suffix=".json", delete=False, encoding="utf-8"
        ) as f:
            json.dump(test_data, f, ensure_ascii=False)
            temp_file_path = f.name

        try:
            categories = load_products_from_json(temp_file_path)
            assert len(categories) == 1
            assert categories[0].name == "Тестовая категория"
            assert "спецсимволами" in categories[0].description
        finally:
            if os.path.exists(temp_file_path):
                os.unlink(temp_file_path)
