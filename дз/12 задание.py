import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №12"
    
    # Создаем текстовые поля для ввода t и x
    t_input = ft.TextField(label="Введите значение для переменной t", keyboard_type=ft.KeyboardType.NUMBER)
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить K", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("K= ", size=20)
    
    def calculate():
        try:
            t = float(t_input.value)
            x = float(x_input.value)
            K = 7 * np.power(t,2) + 3 * np.sin(np.power(x,3)) + 9.2
            result_text.value = f"K = {K}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(t_input, x_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)
