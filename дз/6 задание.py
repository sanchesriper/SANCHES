import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №6"
    
    # Создаем текстовые поля для ввода y и x
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить M", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("M= ", size=20)
    
    def calculate():
        try:
            y = float(y_input.value)
            x = float(x_input.value)
            M = np.cos(2*y) + 3.6 * np.exp(x)
            result_text.value = f"M = {M}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(y_input, x_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)
