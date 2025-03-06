import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №8"
    
    # Создаем текстовые поля для ввода y
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить T", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("T= ", size=20)
    
    def calculate():
        try:
            y = float(y_input.value)
            T = np.sqrt(np.abs(6 * np.power(y,2) - 0.1 * y + 4))
            result_text.value = f"T = {T}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)
