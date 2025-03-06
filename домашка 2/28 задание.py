import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание 28"
    
    # Создаем текстовые поля для ввода v и y
    v_input = ft.TextField(label="Введите значение для переменной v", keyboard_type=ft.KeyboardType.NUMBER)
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить W", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("W= ", size=20)
    
    def calculate():
        try:
            v = float(v_input.value)
            y = float(y_input.value)
            W = 0.004 * v + np.exp(2 * y) / np.exp(y / 2)
            result_text.value = f"W = {W}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()
        except Exception as e:
            result_text.value = f"Ошибка: {str(e)}"
            page.update()

    # Добавляем элементы на страницу
    page.add(v_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)