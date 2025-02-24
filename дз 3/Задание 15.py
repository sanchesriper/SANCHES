import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №15"
    
    # Создаем текстовые поля для ввода m и y
    m_input = ft.TextField(label="Введите значение для переменной m", keyboard_type=ft.KeyboardType.NUMBER)
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить N", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("N = ", size=20)
    
    def calculate():
        try:
            m = float(m_input.value)
            y = float(y_input.value)
            denominator = np.cos(np.radians(2 * y)) + 3.6
            
            # Проверка на деление на ноль
            if denominator == 0:
                result_text.value = "Ошибка: Деление на ноль."
                page.update()
                return
            
            N = (m**2 + 2.8 * m + 0.355) / denominator
            result_text.value = f"N = {N}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(m_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)