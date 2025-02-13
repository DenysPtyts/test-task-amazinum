import random
import matplotlib.pyplot as plt

nums = [random.randint(1, 100) for i in range(20)]
print("Generated list:", nums)

# Функція для знаходження глибини найглибшого озера та його меж
def deepest_lake_depth(heights):
    max_depth = 0
    start_index = 0
    end_index = 0
    n = len(heights)
    
    for i in range(n):
        for j in range(i + 2, n):  # Мінімум 2 значення між вершинами
            if heights[j] > heights[i]:  # Переконуємося, що j — це друга вершина
                min_inside = min(heights[i+1:j])
                lake_depth = min(heights[i], heights[j]) - min_inside
                if lake_depth > max_depth:
                    max_depth = lake_depth
                    start_index = i
                    end_index = j
    
    return max_depth, start_index, end_index

# Обчислення глибини найбільшого озера та його меж
max_lake_depth, start_index, end_index = deepest_lake_depth(nums)
print("Depth of the deepest lake:", max_lake_depth)
print("Start index:", start_index)
print("End index:", end_index)

# Створення графіка
lines = plt.plot(nums, marker='o', linestyle='-', color='b', label='Висоти')  # Зберігаємо об'єкт лінії

# Знаходження найменшого значення
min_value = min(nums)

# Додавання пунктирних ліній найменшого значення
plt.axhline(min_value, color='g', linestyle='--')

# Додавання пунктирної лінії та точки для глибини найбільшого озера
plt.axhline(max_lake_depth, color='r', linestyle='--')

# Змінюємо колір частин існуючої лінії
for line in lines:
    xdata, ydata = line.get_data()
    line.set_data(xdata, ydata)
    line.set_color('b')  # За замовчуванням синій колір

    # Створюємо нову лінію для відображення "озера" червоним кольором
    plt.plot(xdata[start_index:end_index+1], ydata[start_index:end_index+1], marker='o', linestyle='-', color='r')

# Додавання підписів до осей
plt.xlabel('Індекс')
plt.ylabel('Значення')

# Додавання заголовку
plt.title('Графік випадкових чисел')

# Показ графіка
plt.show()