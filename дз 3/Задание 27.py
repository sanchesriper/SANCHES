import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №27"
    
    # Создаем текстовые поля для ввода a, x, y и c
    a_input = ft.TextField(label="Введите значение для переменной a", keyboard_type=ft.KeyboardType.NUMBER)
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    c_input = ft.TextField(label="Введите значение для переменной c", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить P", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("P = ", size=20)
    
    def calculate():
        try:
            a = float(a_input.value)
            x = float(x_input.value)
            y = float(y_input.value)
            c = float(c_input.value)

            # Вычисление P
            arccos_term = np.arccos(a + x**3)  # arccos(a + x^3)
            sin_term = (np.sin(Y - c)**4) / (np.sin(x + y)**3)  # sin^4(Y - c) / sin^3(x + y)
            absolute_term = abs(x - y)  # |x - y|

            P = a**5 + arccos_term - sin_term + absolute_term
            
            result_text.value = f"P = {P}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(a_input, x_input, y_input, c_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)