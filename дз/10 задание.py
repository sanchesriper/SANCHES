import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №10"
    
    # Создаем текстовые поля для ввода k,y и x
    k_input = ft.TextField(label="Введите значение для переменной k", keyboard_type=ft.KeyboardType.NUMBER)
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить U", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("U= ", size=20)
    
    def calculate():
        try:
            k = float(k_input.value)
            y = float(y_input.value)
            x = float(x_input.value)
            U = np.exp(y) + 7.355 * np.power(k,2) + np.power(np.sin(x),2)
            result_text.value = f"U = {U}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(k_input, y_input, x_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)