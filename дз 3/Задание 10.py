import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №10"
    
    # Создаем текстовые поля для ввода x и y
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить U", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("U = ", size=20)
    
    def calculate():
        try:
            x = float(x_input.value)
            y = float(y_input.value)

            # Проверка на деление на ноль
            denominator = np.arctan(x) + 5.2 * y
            if denominator == 0:
                result_text.value = "Ошибка: Деление на ноль."
                page.update()
                return

            U = np.exp(x**3) + (np.cos(x - 4)**2) / denominator
            result_text.value = f"U = {U}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(x_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)