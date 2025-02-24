import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №11"
    
    # Создаем текстовые поля для ввода x и y
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить I", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("I = ", size=20)
    
    def calculate():
        try:
            x = float(x_input.value)
            y = float(y_input.value)
            
            # Проверка на деление на ноль
            denominator = np.exp(y) + np.sin(x)**2
            if denominator == 0:
                result_text.value = "Ошибка: Деление на ноль."
                page.update()
                return
            
            I = (2.33 * np.log(np.sqrt(1 + np.cos(y)**2))) / denominator
            result_text.value = f"I = {I}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(x_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)