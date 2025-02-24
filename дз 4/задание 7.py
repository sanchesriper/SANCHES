import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №7"
    
    # Создаем текстовые поля для ввода x, y и a
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    a_input = ft.TextField(label="Введите значение для переменной a", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить D", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("D = ", size=20)
    
    def calculate():
        try:
            x = float(x_input.value)
            y = float(y_input.value)
            a = float(a_input.value)
            
            # Проверка на деление на ноль
            denominator = np.log(x**4) - 2 * (np.sin(x))**5
            if denominator == 0:
                result_text.value = "Ошибка: Деление на ноль."
                page.update()
                return
            
            D = np.cos(x**3 + 6) - (np.sin(y - a) / denominator)
            result_text.value = f"D = {D}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(x_input, y_input, a_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)