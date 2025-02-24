import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №8"
    
    # Создаем текстовые поля для ввода x, y, a и c
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    a_input = ft.TextField(label="Введите значение для переменной a", keyboard_type=ft.KeyboardType.NUMBER)
    c_input = ft.TextField(label="Введите значение для переменной c", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить P", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("P = ", size=20)
    
    def calculate():
        try:
            x = float(x_input.value)
            y = float(y_input.value)
            a = float(a_input.value)
            c = float(c_input.value)

            # Проверка на деление на ноль
            denominator = np.sin(x + y)**3
            if denominator == 0:
                result_text.value = "Ошибка: Деление на ноль."
                page.update()
                return
            
            P = a**5 + (np.sin(y - c)**4 / denominator) + abs(x - y)
            result_text.value = f"P = {P}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(x_input, y_input, a_input, c_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)