import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №25"
    
    # Создаем текстовые поля для ввода a, x и y
    a_input = ft.TextField(label="Введите значение для переменной a", keyboard_type=ft.KeyboardType.NUMBER)
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить J", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("J = ", size=20)
    
    def calculate():
        try:
            a = float(a_input.value)
            x = float(x_input.value)
            y = float(y_input.value)
            
            # Вычисление J с использованием numpy
            # cot(a) = 1/tan(a)
            cot_term = (1 / np.tan(a ** 3)) ** 3  # cot^3(a^3)
            arctan_term = np.arctan(a) ** 2        # arctan^2(a)
            sqrt_term = np.sqrt(y ** np.tan(x))   # sqrt(y^(tan(x)))

            if sqrt_term == 0:  # Проверка на деление на ноль
                result_text.value = "Ошибка: деление на ноль."
            else:
                J = cot_term + arctan_term / sqrt_term
                result_text.value = f"J = {J}"
            page.update()

        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(a_input, x_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)