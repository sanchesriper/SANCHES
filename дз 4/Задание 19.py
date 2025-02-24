import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №19"
    
    # Создаем текстовые поля для ввода K, a, b, x и y
    k_input = ft.TextField(label="Введите значение для переменной K", keyboard_type=ft.KeyboardType.NUMBER)
    a_input = ft.TextField(label="Введите значение для переменной a", keyboard_type=ft.KeyboardType.NUMBER)
    b_input = ft.TextField(label="Введите значение для переменной b", keyboard_type=ft.KeyboardType.NUMBER)
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить D", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("D = ", size=20)
    
    def calculate():
        try:
            K = float(k_input.value)
            a = float(a_input.value)
            b = float(b_input.value)
            x = float(x_input.value)
            y = float(y_input.value)

            # Вычисление D
            numerator = K**(-a) - np.sqrt(6) - np.cos(3 * a * b)
            denominator = np.sin(a * np.arcsin(x) + np.log(y))**2
            
            if denominator == 0:
                result_text.value = "Ошибка: Деление на ноль."
                page.update()
                return
            
            D = numerator / denominator
            
            result_text.value = f"D = {D}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(k_input, a_input, b_input, x_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)