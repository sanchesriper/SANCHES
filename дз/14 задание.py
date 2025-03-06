import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №14"
    
    # Создаем текстовые поля для ввода y и x
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить R", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("R= ", size=20)
    
    def calculate():
        try:
            y = float(y_input.value)
            x = float(x_input.value)
            R = np.abs(np.sqrt(np.power(np.sin(y),2))) + 6.835 + np.exp(x)
            result_text.value = f"R = {R}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(y_input, x_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)