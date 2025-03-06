import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №2"
    
    # Создаем текстовые поля для ввода p и y
    p_input = ft.TextField(label="Введите значение для переменной p", keyboard_type=ft.KeyboardType.NUMBER)
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить K", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("K= ", size=20)
    
    def calculate():
        try:
            p = float(p_input.value)
            y = float(y_input.value)
            K = np.log10 (np.power(p,2) + np.power (y,3)) + np.exp(p) 
            result_text.value = f"K = {K}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(p_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)
