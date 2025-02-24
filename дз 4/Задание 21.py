import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №21"

    # Создаем текстовые поля для ввода z, x и a
    z_input = ft.TextField(label="Введите значение для переменной z", keyboard_type=ft.KeyboardType.NUMBER)
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)
    a_input = ft.TextField(label="Введите значение для переменной a", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить N", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("N = ", size=20)
    
    def calculate():
        try:
            z = float(z_input.value)
            x = float(x_input.value)
            a = float(a_input.value)

            # Вычисление N
            sqrt_term = np.sqrt(z + np.sqrt(z  x))
            exp_term = np.exp(x) + a**5  np.arctan(x)
            N = (5 * sqrt_term) / exp_term
            result_text.value = f"N = {N}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(z_input, x_input, a_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)