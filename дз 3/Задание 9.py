import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №9"
    
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

            # Проверка на деление на ноль
            denominator = np.exp(y)
            if denominator == 0:
                result_text.value = "Ошибка: Деление на ноль."
                page.update()
                return
            
            R = (np.cos(y)**3) + (2**x * d) / denominator + np.log(np.sin(x)**2 + 7.4)
            result_text.value = f"R = {R}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(x_input, y_input, d_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)