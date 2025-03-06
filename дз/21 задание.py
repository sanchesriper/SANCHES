import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №21"
    
    # Создаем текстовые поля для ввода h и y
    h_input = ft.TextField(label="Введите значение для переменной h", keyboard_type=ft.KeyboardType.NUMBER)
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить P", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("P= ", size=20)
    
    def calculate():
        try:
            h = float(h_input.value)
            y = float(y_input.value)
            P = np.exp(y + 5.5) + 9.1 * np.power(h,3)
            result_text.value = f"P = {P}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(h_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)