import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №3"
    
    # Создаем текстовые поля для ввода n и y
    n_input = ft.TextField(label="Введите значение для переменной n", keyboard_type=ft.KeyboardType.NUMBER)
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить G", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("G= ", size=20)
    
    def calculate():
        try:
            n = float(n_input.value)
            y = float(y_input.value)
            G = n * (y + 3.5) + np.sqrt(y)
            result_text.value = f"G = {G}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(n_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)
