import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №22"
    
    # Создаем текстовые поля для ввода x и y
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить F", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("F = ", size=20)
    
    def calculate():
        try:
            x = float(x_input.value)
            y = float(y_input.value)
            
            # Вычисление F
            cos_term = np.cos(x**2 + 2)
            numerator = 3.5 * x**2 + 1
            cos_squared = np.cos(y)**2
            
            # Проверка на ноль в знаменателе
            if cos_squared == 0:
                result_text.value = "Ошибка: деление на ноль."
            else:
                F = cos_term + (numerator / cos_squared)
                result_text.value = f"F = {F}"
            
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(x_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)