import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №19"
    
    # Создаем текстовые поля для ввода y,g и n
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)
    k_input = ft.TextField(label="Введите значение для переменной k", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить U", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("U= ", size=20)
    
    def calculate():
        try:
            y = float(y_input.value)
            x = float(x_input.value)
            k = float(k_input.value)
            U = np.exp(k + y) + np.tan(x)*np.sqrt(y)
            result_text.value = f"U = {U}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(y_input, x_input, k_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)