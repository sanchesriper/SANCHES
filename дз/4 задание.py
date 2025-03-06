import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №4"
    
    # Создаем текстовые поля для ввода a и t
    a_input = ft.TextField(label="Введите значение для переменной a", keyboard_type=ft.KeyboardType.NUMBER)
    t_input = ft.TextField(label="Введите значение для переменной t", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить D", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("D= ", size=20)
    
    def calculate():
        try:
            a = float(a_input.value)
            t = float(t_input.value)
            D = 9.8 * np.power(a,2) + 5.52 * np.cos(np.power(t,5))
            result_text.value = f"D = {D}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(a_input, t_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)
