import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №5"
    
    # Создаем текстовые поля для ввода x, y и z
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    z_input = ft.TextField(label="Введите значение для переменной z", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить G", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("G = ", size=20)
    
    def calculate():
        try:
            x = float(x_input.value)
            y = float(y_input.value)
            z = float(z_input.value)
            G = np.tan(x**4 - 6) - (np.cos(z + x * y)**3) / (np.cos(x**3)**4 * (y**2))
            result_text.value = f"G = {G}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(x_input, y_input, z_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)