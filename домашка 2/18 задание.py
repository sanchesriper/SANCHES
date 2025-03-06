import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание 18"
    
    # Создаем текстовые поля для ввода y и k
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    k_input = ft.TextField(label="Введите значение для переменной k", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить R", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("R= ", size=20)
    
    def calculate():
        try:
            y = float(y_input.value)
            k = float(k_input.value)
            if y + k <= 0:
                raise ValueError("y + k должно быть больше нуля для вычисления логарифма.")
            R = np.sqrt(np.power(np.sin(y), 2) + 6.835) / np.log(y + k) + 3 * np.power(y, 2)
            result_text.value = f"R = {R}"
            page.update()
        except ValueError as ve:
            result_text.value = f"Ошибка: {ve}"
            page.update()
        except Exception as e:
            result_text.value = f"Ошибка: {str(e)}"
            page.update()

    # Добавляем элементы на страницу
    page.add(y_input, k_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)