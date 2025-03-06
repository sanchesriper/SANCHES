import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №25"
    
    # Создаем текстовые поля для ввода y и f
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    f_input = ft.TextField(label="Введите значение для переменной f", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить G", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("G= ", size=20)
    
    def calculate():
        try:
            y = float(y_input.value)
            f = float(f_input.value)
            G = np.exp(2 * y) + np.sin(np.power(f,2))
            result_text.value = f"G = {G}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(y_input, f_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)
