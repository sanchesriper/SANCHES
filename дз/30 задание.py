import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №30"
    
    # Создаем текстовые поля для ввода y и r
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    r_input = ft.TextField(label="Введите значение для переменной r", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить W", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("W= ", size=20)
    
    def calculate():
        try:
            y = float(y_input.value)
            r = float(r_input.value)
            W = np.exp(y + r) + 7.2 * np.sin(r)
            result_text.value = f"W = {W}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(y_input, r_input, calculate_button, result_text)
# Запускаем приложение
ft.app(target=main)
