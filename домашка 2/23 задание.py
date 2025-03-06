import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание 23"
    
    # Создаем текстовые поля для ввода y и d
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    d_input = ft.TextField(label="Введите значение для переменной d", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить R", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("R= ", size=20)
    
    def calculate():
        try:
            y = float(y_input.value)
            d = float(d_input.value)
            
            # Проверка на допустимость логарифма
            if d <= 0:
                raise ValueError("d должно быть больше нуля для вычисления логарифма.")
            
            # Вычисление R
            R = np.power(np.sin(y), 2) + (0.3 * d) / (np.exp(y) + np.log(d))
            result_text.value = f"R = {R}"
            page.update()
        except ValueError as ve:
            result_text.value = f"Ошибка: {ve}"
            page.update()
        except Exception as e:
            result_text.value = f"Ошибка: {str(e)}"
            page.update()

    # Добавляем элементы на страницу
    page.add(y_input, d_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)