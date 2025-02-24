import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №30"
    
    # Создаем текстовые поля для ввода x
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить K", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("K = ", size=20)
    
    def calculate():
        try:
            x = float(x_input.value)
            # Вычисление K
            K = np.sqrt(((3 + x)**6 - np.log(x)) + np.arcsin(6 * x**2))
            result_text.value = f"K = {K}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(x_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)