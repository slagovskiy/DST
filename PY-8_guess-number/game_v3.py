"""
Игра угадай число
Компьютер сам загадывает и сам угадывает число
Используется метод деления пополам
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """
    Случайным образом загадываем 'опортное' число,
    а дальше следуем подсказкам внутреннего голоса,
    который говорит 'больше' или 'меньше'.

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    left = 1    # левая граница
    right = 101   # правая граница
    predict_number = np.random.randint(left, right + 1)  # опорное число
    while True:
        count += 1
        if number == predict_number:
            break   # выход из цикла если угадали
        # если не угадали, то слушем внетренний голос
        # и определяем границу для поиска путем
        # деления интервала от опорного числа до границы пополам
        if number < predict_number:     # нужно меньше
            right = predict_number
        if number > predict_number:     # нужно больше
            left = predict_number
        predict_number = int((right - left) / 2) + left

    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # RUN
    score_game(random_predict)
