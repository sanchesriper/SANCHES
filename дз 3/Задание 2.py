import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №2"
    
    # Создаем текстовые поля для ввода c, x и t
    c_input = ft.TextField(label="Введите значение для переменной c", keyboard_type=ft.KeyboardType.NUMBER)
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)
    t_input = ft.TextField(label="Введите значение для переменной t", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить L", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("L = ", size=20)
    
    def calculate():
        try:
            c = float(c_input.value)
            x = float(x_input.value)
            t = float(t_input.value)
            L = (1 / np.cos(c))**2 + 2 * (x**2) + 5 / np.sqrt(c + t)
            result_text.value = f"L = {L}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()
        except Exception as e:
            result_text.value = f"Ошибка: {str(e)}"
            page.update()

    # Добавляем элементы на страницу
    page.add(c_input, x_input, t_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)