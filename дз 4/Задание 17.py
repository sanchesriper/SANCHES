import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №17"
    
    # Создаем текстовые поля для ввода x, y, a и b
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    a_input = ft.TextField(label="Введите значение для переменной a", keyboard_type=ft.KeyboardType.NUMBER)
    b_input = ft.TextField(label="Введите значение для переменной b", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить T", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("T = ", size=20)
    
    def calculate():
        try:
            x = float(x_input.value)
            y = float(y_input.value)
            a = float(a_input.value)
            b = float(b_input.value)

            # Вычисление T
            log_term = np.log(y)
            arctan_term = np.arctan(b + a)
            T = np.sqrt(x + b - a) + log_term / arctan_term
            
            result_text.value = f"T = {T}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()
        except ZeroDivisionError:
            result_text.value = "Ошибка: Деление на ноль."
            page.update()

    # Добавляем элементы на страницу
    page.add(x_input, y_input, a_input, b_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)