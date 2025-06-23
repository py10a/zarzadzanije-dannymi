#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Лабораторна робота 1: Робота з JSON у Python
Приклади роботи з JSON файлами
"""

import json
import os
from typing import Dict, List, Any

def load_json_file(file_path: str) -> Dict[str, Any]:
    """
    Завантаження JSON файлу
    
    Args:
        file_path (str): Шлях до JSON файлу
        
    Returns:
        Dict[str, Any]: Завантажений словник
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
        print(f"✅ Файл {file_path} успішно завантажено")
        return data
    except FileNotFoundError:
        print(f"❌ Файл {file_path} не знайдено")
        return {}
    except json.JSONDecodeError as e:
        print(f"❌ Помилка декодування JSON: {e}")
        return {}

def save_json_file(data: Dict[str, Any], file_path: str, indent: int = 2) -> bool:
    """
    Збереження даних у JSON файл
    
    Args:
        data (Dict[str, Any]): Дані для збереження
        file_path (str): Шлях до файлу
        indent (int): Відступ для форматування
        
    Returns:
        bool: True якщо збереження успішне
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, ensure_ascii=False, indent=indent)
        print(f"✅ Дані збережено у файл {file_path}")
        return True
    except Exception as e:
        print(f"❌ Помилка збереження: {e}")
        return False

def analyze_json_structure(data: Dict[str, Any], max_items: int = 5) -> None:
    """
    Аналіз структури JSON даних
    
    Args:
        data (Dict[str, Any]): Дані для аналізу
        max_items (int): Максимальна кількість елементів для показу
    """
    print("\n📊 АНАЛІЗ СТРУКТУРИ JSON:")
    print(f"Тип даних: {type(data)}")
    print(f"Кількість елементів: {len(data)}")
    
    if isinstance(data, dict):
        print(f"Ключі (перші {min(max_items, len(data))}):")
        for i, key in enumerate(list(data.keys())[:max_items]):
            value = data[key]
            print(f"  {i+1}. '{key}' -> {type(value).__name__}: {str(value)[:50]}...")
        
        if len(data) > max_items:
            print(f"  ... та ще {len(data) - max_items} елементів")
    
    elif isinstance(data, list):
        print(f"Елементи (перші {min(max_items, len(data))}):")
        for i, item in enumerate(data[:max_items]):
            print(f"  {i+1}. {type(item).__name__}: {str(item)[:50]}...")
        
        if len(data) > max_items:
            print(f"  ... та ще {len(data) - max_items} елементів")

def search_in_json(data: Dict[str, Any], search_term: str) -> List[tuple]:
    """
    Пошук у JSON даних
    
    Args:
        data (Dict[str, Any]): Дані для пошуку
        search_term (str): Термін для пошуку
        
    Returns:
        List[tuple]: Список знайдених пар (ключ, значення)
    """
    results = []
    search_term_lower = search_term.lower()
    
    if isinstance(data, dict):
        for key, value in data.items():
            # Пошук у ключі
            if search_term_lower in key.lower():
                results.append((key, value))
            # Пошук у значенні (якщо це рядок)
            elif isinstance(value, str) and search_term_lower in value.lower():
                results.append((key, value))
            # Пошук у списку значень
            elif isinstance(value, list):
                for item in value:
                    if isinstance(item, str) and search_term_lower in item.lower():
                        results.append((key, value))
                        break
    
    return results

def filter_json_data(data: Dict[str, Any], filter_func) -> Dict[str, Any]:
    """
    Фільтрація JSON даних за функцією
    
    Args:
        data (Dict[str, Any]): Дані для фільтрації
        filter_func: Функція фільтрації (key, value) -> bool
        
    Returns:
        Dict[str, Any]: Відфільтровані дані
    """
    return {key: value for key, value in data.items() if filter_func(key, value)}

def create_sample_json() -> Dict[str, Any]:
    """
    Створення прикладу JSON структури
    
    Returns:
        Dict[str, Any]: Приклад JSON даних
    """
    sample_data = {
        "users": [
            {
                "id": 1,
                "name": "Іван Петренко",
                "email": "ivan@example.com",
                "age": 25,
                "is_active": True,
                "hobbies": ["програмування", "читання", "спорт"]
            },
            {
                "id": 2,
                "name": "Марія Коваленко",
                "email": "maria@example.com",
                "age": 30,
                "is_active": False,
                "hobbies": ["музика", "подорожі"]
            }
        ],
        "settings": {
            "language": "uk",
            "theme": "dark",
            "notifications": True
        },
        "metadata": {
            "created_at": "2024-01-15T10:30:00Z",
            "version": "1.0.0",
            "author": "Лабораторна робота"
        }
    }
    return sample_data

def main():
    """Головна функція з прикладами роботи з JSON"""
    print("🔧 ПРИКЛАДИ РОБОТИ З JSON У PYTHON")
    print("=" * 50)
    
    # 1. Завантаження існуючого JSON файлу
    print("\n1️⃣ ЗАВАНТАЖЕННЯ JSON ФАЙЛУ:")
    data = load_json_file("data.json")
    
    if data:
        analyze_json_structure(data, max_items=3)
        
        # 2. Пошук у даних
        print("\n2️⃣ ПОШУК У JSON ДАНИХ:")
        search_results = search_in_json(data, "computer")
        print(f"Знайдено {len(search_results)} результатів для 'computer':")
        for i, (key, value) in enumerate(search_results[:3]):
            print(f"  {i+1}. Ключ: '{key}'")
            if isinstance(value, list):
                print(f"     Значення: {value[0] if value else 'пустий список'}...")
            else:
                print(f"     Значення: {str(value)[:100]}...")
        
        # 3. Фільтрація даних
        print("\n3️⃣ ФІЛЬТРАЦІЯ JSON ДАНИХ:")
        # Фільтр: тільки ключі, що містять "computer"
        computer_terms = filter_json_data(data, lambda k, v: "computer" in k.lower())
        print(f"Ключі з 'computer': {list(computer_terms.keys())[:5]}")
        
        # Фільтр: тільки короткі значення (менше 50 символів)
        short_values = filter_json_data(data, lambda k, v: isinstance(v, str) and len(v) < 50)
        print(f"Короткі значення (перші 3): {list(short_values.items())[:3]}")
    
    # 4. Створення нового JSON
    print("\n4️⃣ СТВОРЕННЯ НОВОГО JSON:")
    sample_data = create_sample_json()
    print("Створено приклад JSON структури:")
    print(json.dumps(sample_data, ensure_ascii=False, indent=2))
    
    # 5. Збереження у файл
    print("\n5️⃣ ЗБЕРЕЖЕННЯ JSON У ФАЙЛ:")
    save_json_file(sample_data, "sample_output.json")
    
    # 6. Робота з JSON рядками
    print("\n6️⃣ РОБОТА З JSON РЯДКАМИ:")
    json_string = '{"name": "Тест", "numbers": [1, 2, 3], "nested": {"key": "value"}}'
    print(f"JSON рядок: {json_string}")
    
    # Парсинг JSON рядка
    parsed_data = json.loads(json_string)
    print(f"Парсовані дані: {parsed_data}")
    
    # Конвертація назад у рядок
    back_to_string = json.dumps(parsed_data, ensure_ascii=False, indent=2)
    print(f"Повернення у рядок:\n{back_to_string}")
    
    # 7. Обробка помилок
    print("\n7️⃣ ОБРОБКА ПОМИЛОК:")
    invalid_json = '{"name": "Тест", "numbers": [1, 2, 3], "nested": {"key": "value"}'  # Відсутня закриваюча дужка
    try:
        json.loads(invalid_json)
    except json.JSONDecodeError as e:
        print(f"❌ Помилка JSON: {e}")
    
    print("\n✅ Всі приклади завершено!")

if __name__ == "__main__":
    main()
