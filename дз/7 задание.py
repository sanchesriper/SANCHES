import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №7"
    
    # Создаем текстовые поля для ввода m
    m_input = ft.TextField(label="Введите значение для переменной m", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить N", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("N= ", size=20)
    
    def calculate():
        try:
            m = float(m_input.value)
            N = np.power(m,2) + 2.8 * np.abs(m) + 0.55
            result_text.value = f"N = {N}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(m_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)
