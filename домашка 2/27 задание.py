import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание 27"
    
    # Создаем текстовые поля для ввода p и y
    p_input = ft.TextField(label="Введите значение для переменной p", keyboard_type=ft.KeyboardType.NUMBER)
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить Z", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("Z = ", size=20)
    
    def calculate():
        try:
            p = float(p_input.value)
            y = float(y_input.value)
            
            # Проверяем, чтобы знаменатель не был равен нулю
            denominator = np.power(y, 2) + 7.325 * p
            if denominator == 0:
                raise ValueError("Знаменатель не может быть равен нулю.")
            
            # Вычисление Z
            Z = np.power(np.sin(p + 0.4), 2) / denominator
            result_text.value = f"Z = {Z}"
            page.update()
        except ValueError as ve:
            result_text.value = f"Ошибка: {ve}"
            page.update()
        except Exception as e:
            result_text.value = f"Ошибка: {str(e)}"
            page.update()

    # Добавляем элементы на страницу
    page.add(p_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)