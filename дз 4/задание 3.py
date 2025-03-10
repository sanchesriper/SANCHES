import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №3"
    
    # Создаем текстовые поля для ввода y и h
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    h_input = ft.TextField(label="Введите значение для переменной h", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить A", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("A = ", size=20)
    
    def calculate():
        try:
            y = float(y_input.value)
            h = float(h_input.value)
            A = np.tan(y**3 - h**4) + h**2 / (np.sin(h)**3 + y)
            result_text.value = f"A = {A}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(y_input, h_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)