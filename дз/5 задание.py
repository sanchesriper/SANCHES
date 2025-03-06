import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №5"
    
    # Создаем текстовые поля для ввода x
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить L", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("L= ", size=20)
    
    def calculate():
        try:
            x = float(x_input.value)
            L = 1.51 * np.cos(np.power(x,2)) + 2 * np.power(x,3)
            result_text.value = f"L = {L}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(x_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)
