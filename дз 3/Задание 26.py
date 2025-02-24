import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "задание №26"

    # Создаем текстовые поля для ввода x, y и k
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    k_input = ft.TextField(label="Введите значение для переменной k", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить U", on_click=lambda e: calculate())

    # Поле для отображения результата
    result_text = ft.Text("U = ", size=20)

    def calculate():
        try:
            x = float(x_input.value)
            y = float(y_input.value)
            k = float(k_input.value)

            # Вычисление U
            ln_term = np.log(x**3 + y)                # ln(x^3 + y)
            exponential_term = np.exp(y)              # e^y
            fraction = y**4 / exponential_term         # y^4 / e^y
            k_term = 5.4 * k**3                        # 5.4 * k^3

            U = ln_term - fraction + k_term
            result_text.value = f"U = {U}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(x_input, y_input, k_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)