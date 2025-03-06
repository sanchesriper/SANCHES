import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание 22"
    
    # Создаем текстовые поля для ввода t и y
    t_input = ft.TextField(label="Введите значение для переменной t", keyboard_type=ft.KeyboardType.NUMBER)
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить S", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("S= ", size=20)
    
    def calculate():
        try:
            t = float(t_input.value)
            y = float(y_input.value)
            
            # Проверка на допустимость логарифма
            if t <= 0:
                raise ValueError("t должно быть больше нуля для вычисления логарифма.")
            
            # Вычисление S
            S = 4.351 * np.power(y, 3) + (2 * t * np.log(t)) / np.sqrt(np.cos(2 * y) + 4.351)
            result_text.value = f"S = {S}"
            page.update()
        except ValueError as ve:
            result_text.value = f"Ошибка: {ve}"
            page.update()
        except Exception as e:
            result_text.value = f"Ошибка: {str(e)}"
            page.update()

    # Добавляем элементы на страницу
    page.add(t_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)