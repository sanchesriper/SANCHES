import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание 26"
    
    # Создаем текстовые поля для ввода u и y
    u_input = ft.TextField(label="Введите значение для переменной u", keyboard_type=ft.KeyboardType.NUMBER)
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить T", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("T = ", size=20)
    
    def calculate():
        try:
            u = float(u_input.value)
            y = float(y_input.value)
            
            # Проверяем, чтобы (2y + u) было больше нуля для логарифма
            if 2 * y + u <= 0:
                raise ValueError("Аргумент логарифма должен быть больше нуля.")

            # Вычисление T
            T = np.sin(2 * u) / np.log(2 * y + u)
            result_text.value = f"T = {T}"
            page.update()
        except ValueError as ve:
            result_text.value = f"Ошибка: {ve}"
            page.update()
        except Exception as e:
            result_text.value = f"Ошибка: {str(e)}"
            page.update()

    # Добавляем элементы на страницу
    page.add(u_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)