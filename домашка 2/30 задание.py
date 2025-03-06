import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание 30"
    
    # Создаем текстовые поля для ввода y и p
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    p_input = ft.TextField(label="Введите значение для переменной p", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить N", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("N = ", size=20)
    
    def calculate():
        try:
            y = float(y_input.value)
            p = float(p_input.value)
            N = 3 * np.power(y, 2) + np.sqrt(y + 1) / (np.log(p + y) + np.exp(p))
            result_text.value = f"N = {N}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()
        except Exception as e:
            result_text.value = f"Ошибка: {str(e)}"
            page.update()

    # Добавляем элементы на страницу
    page.add(y_input, p_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)