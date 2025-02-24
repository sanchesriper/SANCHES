import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №1"
    
    # Создаем текстовые поля для ввода x и a
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)
    a_input = ft.TextField(label="Введите значение для переменной a", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить L", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("L = ", size=20)
    
    def calculate():
        try:
            x = float(x_input.value)
            a = float(a_input.value)
            L = (np.sqrt(np.exp(x) - np.cos(x**(4 * a**5))) + np.arctan(a - x**5)**4) / np.sqrt(np.abs(a + x**4))
            result_text.value = f"L = {L}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(x_input, a_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)