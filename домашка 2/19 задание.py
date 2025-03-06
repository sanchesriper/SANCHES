import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание 19"
    
    # Создаем текстовые поля для ввода y и q
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    q_input = ft.TextField(label="Введите значение для переменной q", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить E", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("E= ", size=20)
    
    def calculate():
        try:
            y = float(y_input.value)
            q = float(q_input.value)
            
            # Проверка на допустимость логарифма
            if 0.7 * y + 2 * q <= 0:
                raise ValueError("0.7y + 2q должно быть больше нуля для вычисления логарифма.")
            
            # Вычисление формулы
            E = np.log(0.7 * y + 2 * q) / np.sqrt(3 * np.power(y, 2) + 0.5 * y + 4)
            result_text.value = f"E = {E}"
            page.update()
        except ValueError as ve:
            result_text.value = f"Ошибка: {ve}"
            page.update()
        except Exception as e:
            result_text.value = f"Ошибка: {str(e)}"
            page.update()

    # Добавляем элементы на страницу
    page.add(y_input, q_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)