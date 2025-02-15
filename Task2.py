import numpy as np

def count_live_neighbors(matrix, x, y):
    neighbors = [
        (-1, -1), (-1, 0), (-1, 1),  # Верхні сусіди
        (0, -1),         (0, 1),      # Лівий і правий сусід
        (1, -1), (1, 0), (1, 1)       # Нижні сусіди
    ]

    count = 0
    for dx, dy in neighbors:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 20 and 0 <= ny < 20: # Перевіряємо, що сусід у межах матриці
            count += matrix[nx, ny]
        
    return count

def next_gen(matrix):
    new_matrix = np.zeros((20, 20), dtype=int)

    for i in range(20):
        for j in range(20):
            live_neighbors = count_live_neighbors(matrix, i, j)
            
            if matrix[i, j] == 1:  # Якщо клітина жива
                if live_neighbors < 2:  
                    new_matrix[i, j] = 0  # Помирає від самотності (менше 2 сусідів)
                elif live_neighbors in [2, 3]:  
                    new_matrix[i, j] = 1  # Виживає (2 або 3 сусіди)
                elif live_neighbors >= 4:  
                    new_matrix[i, j] = 0  # Помирає від перенаселення (4 або більше сусідів)
            else:  # Якщо клітина мертва
                if live_neighbors == 3:
                    new_matrix[i, j] = 1  # Оживає

    return new_matrix

matrix = np.random.randint(0, 2, (20, 20))

print("Primery matrix: \n", matrix)

matrix = next_gen(matrix)

print("New matrix: \n",matrix)