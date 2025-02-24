import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №13"
    
    # Создаем текстовые поля для ввода x, a и b
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)
    a_input = ft.TextField(label="Введите значение для переменной a", keyboard_type=ft.KeyboardType.NUMBER)
    b_input = ft.TextField(label="Введите значение для переменной b", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить R", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("R = ", size=20)
    
    def calculate():
        try:
            x = float(x_input.value)
            a = float(a_input.value)
            b = float(b_input.value)

            # Проверка на деление на ноль
            if a <= 0:
                result_text.value = "Ошибка: a должно быть положительным для логарифма."
                page.update()
                return
            
            denominator = np.log(a)**3
            if denominator == 0:
                result_text.value = "Ошибка: Деление на ноль в логарифме."
                page.update()
                return
            
            R = (a / x) - a + (b ** x) + (np.cos(x)**3 / denominator) + 4.5
            result_text.value = f"R = {R}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(x_input, a_input, b_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)