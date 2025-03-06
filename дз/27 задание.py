import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №27"
    
    # Создаем текстовые поля для ввода y,v и x
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    v_input = ft.TextField(label="Введите значение для переменной v", keyboard_type=ft.KeyboardType.NUMBER)
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить W", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("W= ", size=20)
    
    def calculate():
        try:
            y = float(y_input.value)
            v = float(v_input.value)
            x = float(x_input.value)
            W = 1.03 * v + np.exp(2 * y) + np.tan(np.abs(x))
            result_text.value = f"W = {W}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(y_input, v_input, x_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)