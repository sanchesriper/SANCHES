import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №20"
    
    # Создаем текстовые поля для ввода y, x, a, b и c
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)
    a_input = ft.TextField(label="Введите значение для переменной a", keyboard_type=ft.KeyboardType.NUMBER)
    b_input = ft.TextField(label="Введите значение для переменной b", keyboard_type=ft.KeyboardType.NUMBER)
    c_input = ft.TextField(label="Введите значение для переменной c", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить U", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("U = ", size=20)
    
    def calculate():
        try:
            y = float(y_input.value)
            x = float(x_input.value)
            a = float(a_input.value)
            b = float(b_input.value)
            c = float(c_input.value)

            # Вычисление U
            tan_term = np.tan(y)**3
            sin_term = np.sin(x)**5
            sqrt_b_c = np.sqrt(b - c) if b - c >= 0 else 0  # Проверка на неотрицательность
            sqrt_a_b_c = np.sqrt(a - b + c) if a - b + c > 0 else 1  # Проверка на положительность
            
            U = tan_term + (sin_term * sqrt_b_c) / sqrt_a_b_c
            
            result_text.value = f"U = {U}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(y_input, x_input, a_input, b_input, c_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)