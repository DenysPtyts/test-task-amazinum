import numpy as np

# Ймовірності випадіння 'H' для кожної монети
p_heads = np.array([0.8, 0.9, 0.1, 0.2, 0.3])
p_tails = 1 - p_heads

# Початкові ймовірності вибору кожної монети
p_coins = np.array([0.2] * 5)

# Послідовність підкидань: [H, T, H, H, H, T, T, H, H]
flips = ['H', 'T', 'H', 'H', 'H', 'T', 'T', 'H', 'H']

# Зберігаємо ймовірності випадіння 'H' після кожного підкидання
prob_H_next = []

# Оновлення ймовірностей крок за кроком
for flip in flips:
    if flip == 'H':
        p_total = np.sum(p_heads * p_coins)
        p_coins = (p_heads * p_coins) / p_total  # Оновлення ймовірностей
    else:  # flip == 'T'
        p_total = np.sum(p_tails * p_coins)
        p_coins = (p_tails * p_coins) / p_total  # Оновлення ймовірностей

    # Обчислюємо ймовірність випадіння 'H' у наступному підкиданні
    prob_H_next.append(float(round(np.sum(p_heads * p_coins), 2)))

print(prob_H_next)
