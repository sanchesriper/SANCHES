import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №29"
    
    # Создаем текстовые поля для ввода x, y и d
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    d_input = ft.TextField(label="Введите значение для переменной d", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить R", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("R = ", size=20)
    
    def calculate():
        try:
            x = float(x_input.value)
            y = float(y_input.value)
            d = float(d_input.value)

            # Вычисление R
            numerator = np.cos(y)**2 + 2.4 * d  # cos^2(y) + 2.4d
            denominator = np.exp(y) + np.log(np.sin(x)**2 + 6)  # e^y + ln(sin^2(x) + 6)
            R = numerator / denominator
            
            result_text.value = f"R = {R}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(x_input, y_input, d_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)