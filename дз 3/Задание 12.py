import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №12"
    
    # Создаем текстовые поля для ввода x, y, a и f
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    a_input = ft.TextField(label="Введите значение для переменной a", keyboard_type=ft.KeyboardType.NUMBER)
    f_input = ft.TextField(label="Введите значение для переменной f", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить G", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("G = ", size=20)
    
    def calculate():
        try:
            x = float(x_input.value)
            y = float(y_input.value)
            a = float(a_input.value)
            f = float(f_input.value)

            # Проверка на деление на ноль
            denominator = np.arctan((x + a)**4) * (x**5)
            if denominator == 0:
                result_text.value = "Ошибка: Деление на ноль."
                page.update()
                return
            
            G = (np.cos(f)**3 * abs(y + x)) - ((x + y) / denominator)
            result_text.value = f"G = {G}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(x_input, y_input, a_input, f_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)