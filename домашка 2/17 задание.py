import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание 17"
    
    # Создаем текстовые поля для ввода y и n
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    n_input = ft.TextField(label="Введите значение для переменной n", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить H", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("H= ", size=20)
    
    def calculate():
        try:
            y = float(y_input.value)
            n = float(n_input.value)
            # Проверяем, чтобы n не был равен 0
            if n == 0:
                raise ValueError("n не должен быть равен нулю для избежания деления на ноль.")
            H = np.power(y, 2) - 0.8 * y + np.sqrt(y) / (23.1 * np.power(n, 2) + np.cos(n))
            result_text.value = f"H = {H}"
            page.update()
        except ValueError as ve:
            result_text.value = f"Ошибка: {ve}"
            page.update()

    # Добавляем элементы на страницу
    page.add(y_input, n_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)