import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №1"
    
    # Создаем текстовые поля для ввода t и l
    t_input = ft.TextField(label="Введите значение для переменной t", keyboard_type=ft.KeyboardType.NUMBER)
    l_input = ft.TextField(label="Введите значение для переменной l", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить R", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("R= ", size=20)
    
    def calculate():
        try:
            t = float(t_input.value)
            l = float(l_input.value)
            R = 3 * np.power(t, 2) + 3 * np.power(l, 5) + 4.9
            result_text.value = f"R = {R}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(t_input, l_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)
