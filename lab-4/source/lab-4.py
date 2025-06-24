import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

reviews_location = "/Users/py10/projects/zarzadzanije-dannymi/lab-4/reviews_courses.csv"

# Завантаження даних
reviews = pd.read_csv(reviews_location)

# Конвертуємо Timestamp в datetime
reviews['Timestamp'] = pd.to_datetime(reviews['Timestamp'])

# Створюємо колонку з датою (без часу)
reviews['Date'] = reviews['Timestamp'].dt.date
reviews['Week'] = reviews['Timestamp'].dt.strftime('%Y-%U')

# Групуємо за датою та обчислюємо середній рейтинг
daily_ratings = reviews.groupby('Date')['Rating'].mean().reset_index()
daily_ratings = daily_ratings.sort_values('Date')

weekly_ratings = reviews.groupby('Week')['Rating'].mean().reset_index()
weekly_ratings = weekly_ratings.sort_values('Week')

# # Створюємо графік
# plt.figure(figsize=(15, 8))
# plt.plot(daily_ratings['Date'], daily_ratings['Rating'], marker='o', linewidth=2, markersize=4, color='blue', alpha=0.7)

# Створюємо графік
plt.figure(figsize=(15, 8))
plt.plot(weekly_ratings['Week'], weekly_ratings['Rating'], marker='o', linewidth=2, markersize=4, color='blue', alpha=0.7)

# Налаштування графіка
plt.title('Середній рейтинг курсів за днями', fontsize=16, fontweight='bold')
plt.xlabel('Дата', fontsize=12)
plt.ylabel('Середній рейтинг', fontsize=12)
plt.grid(True, alpha=0.3)

# Поворот підписів дат для кращої читабельності
plt.xticks(rotation=45, ha='right')

# Додаємо горизонтальну лінію для середнього рейтингу
overall_avg = reviews['Rating'].mean()
plt.axhline(y=overall_avg, color='red', linestyle='--', alpha=0.7, label=f'Загальний середній: {overall_avg:.2f}')

plt.legend()
plt.tight_layout()
plt.show()

# Виводимо статистику
print(f"Загальна кількість днів: {len(daily_ratings)}")
print(f"Загальний середній рейтинг: {overall_avg:.2f}")
print(f"Найвищий середній рейтинг за день: {daily_ratings['Rating'].max():.2f}")
print(f"Найнижчий середній рейтинг за день: {daily_ratings['Rating'].min():.2f}")

