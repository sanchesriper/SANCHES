import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №14"
    
    # Создаем текстовое поле для ввода x
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить R", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("R = ", size=20)
    
    def calculate():
        try:
            x = float(x_input.value)
            # Вычисление R
            sin_x2_plus_4 = np.sin(x**2 + 4)**3
            sin_x4 = np.sin(x**4)**3
            
            # Проверка на деление на ноль
            if sin_x4 == 0:
                result_text.value = "Ошибка: Деление на ноль."
                page.update()
                return
            
            R = sin_x2_plus_4 + (4.3 / sin_x4)
            result_text.value = f"R = {R}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(x_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)