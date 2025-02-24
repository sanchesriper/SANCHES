import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "задание №23"
    
    # Создаем текстовые поля для ввода x, z, a и b
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)
    z_input = ft.TextField(label="Введите значение для переменной z", keyboard_type=ft.KeyboardType.NUMBER)
    a_input = ft.TextField(label="Введите значение для переменной a", keyboard_type=ft.KeyboardType.NUMBER)
    b_input = ft.TextField(label="Введите значение для переменной b", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить F", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("F = ", size=20)
    
    def calculate():
        try:
            x = float(x_input.value)
            z = float(z_input.value)
            a = float(a_input.value)
            b = float(b_input.value)

            # Вычисление F
            numerator = np.sqrt(np.abs(x) + np.cos(x)**3 + z**4)
            ln_term = np.log(x)
            arcsin_term = np.arcsin(b * x - a)

            # Проверка на деление на ноль
            if ln_term - arcsin_term == 0:
                result_text.value = "Ошибка: деление на ноль."
            else:
                F = numerator / (ln_term - arcsin_term)
                result_text.value = f"F = {F}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(x_input, z_input, a_input, b_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)