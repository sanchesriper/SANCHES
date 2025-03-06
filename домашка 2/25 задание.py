import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание 25"
    
    # Создаем текстовые поля для ввода c и t
    c_input = ft.TextField(label="Введите значение для переменной c", keyboard_type=ft.KeyboardType.NUMBER)
    t_input = ft.TextField(label="Введите значение для переменной t", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить L", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("L = ", size=20)
    
    def calculate():
        try:
            c = float(c_input.value)
            t = float(t_input.value)
            
            # Проверяем, чтобы c + t было больше нуля для вычисления корня
            if c + t <= 0:
                raise ValueError("c + t должно быть больше нуля для вычисления квадратного корня.")
            
            # Вычисление L
            L = np.power(np.cos(c), 2) + 3 * np.power(t, 2) + 4 / np.sqrt(c + t)
            result_text.value = f"L = {L}"
            page.update()
        except ValueError as ve:
            result_text.value = f"Ошибка: {ve}"
            page.update()

    # Добавляем элементы на страницу
    page.add(c_input, t_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)
                                                                                                                                                                 