import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №19"
    
    # Создаем текстовые поля для ввода y,g и n
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    g_input = ft.TextField(label="Введите значение для переменной g", keyboard_type=ft.KeyboardType.NUMBER)
    n_input = ft.TextField(label="Введите значение для переменной n", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить P", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("P= ", size=20)
    
    def calculate():
        try:
            y = float(y_input.value)
            g = float(g_input.value)
            n = float(n_input.value)
            P = n * np.sqrt(np.power(y,3) + 1.09 * g)
            result_text.value = f"P = {P}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(y_input, g_input, n_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)