import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №24"
    
    # Создаем текстовые поля для ввода x, a и b
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)
    a_input = ft.TextField(label="Введите значение для переменной a", keyboard_type=ft.KeyboardType.NUMBER)
    b_input = ft.TextField(label="Введите значение для переменной b", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить F", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("F = ", size=20)
    
    def calculate():
        try:
            x = float(x_input.value)
            a = float(a_input.value)
            b = float(b_input.value)

            # Вычисление F
            cos_term = np.cos(b * x**5)**7
            sin_term = np.sin(a**2)
            cos_inner_term = np.cos(x**3 + x**5 - a**2)
            arcsin_term = np.arcsin(a**2)
            arccos_term = np.arccos(x**7 - a**2)

            # Проверка на допустимость значений для arcsin и arccos
            if arcsin_term is None or arccos_term is None:
                result_text.value = "Ошибка: недопустимые значения для arcsin или arccos."
                page.update()
                return

            denominator = arcsin_term + arccos_term
            
            # Проверка на деление на ноль
            if denominator == 0:
                result_text.value = "Ошибка: деление на ноль."
            else:
                F = cos_term - (sin_term + cos_inner_term) / denominator
                result_text.value = f"F = {F}"
            
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(x_input, a_input, b_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)