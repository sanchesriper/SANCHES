import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №26"
    
    # Создаем текстовые поля для ввода p
    p_input = ft.TextField(label="Введите значение для переменной p", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить Z", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("Z= ", size=20)
    
    def calculate():
        try:
            p = float(p_input.value)
            Z = np.power(np.sin(np.power(p,2) + 0.4),3)
            result_text.value = f"Z = {Z}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(p_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)
