import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание 29"
    
    # Создаем текстовые поля для ввода h и y
    h_input = ft.TextField(label="Введите значение для переменной h", keyboard_type=ft.KeyboardType.NUMBER)
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить T", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("T = ", size=20)
    
    def calculate():
        try:
            h = float(h_input.value)
            y = float(y_input.value)
            T = 0.355 * np.power(h, 2) - 4.355 / np.exp(y + h) + np.sqrt(2.7 * y)
            result_text.value = f"T = {T}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()
        except Exception as e:
            result_text.value = f"Ошибка: {str(e)}"
            page.update()

    # Добавляем элементы на страницу
    page.add(h_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)