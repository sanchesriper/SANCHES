import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание №18"
    
    # Создаем текстовые поля для ввода y и t
    y_input = ft.TextField(label="Введите значение для переменной y", keyboard_type=ft.KeyboardType.NUMBER)
    t_input = ft.TextField(label="Введите значение для переменной t", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить S", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("S = ", size=20)
    
    def calculate():
        try:
            y = float(y_input.value)
            t = float(t_input.value)
            
            # Вычисление S
            log_term = 2 * t * np.log(t)
            cos_term = np.sqrt(np.cos(2 * y))
            
            # Проверка на деление на ноль
            if cos_term == 0:
                result_text.value = "Ошибка: Деление на ноль."
                page.update()
                return
            
            S = 4.351 * np.power(y, 3) + log_term / cos_term + 4.351
            result_text.value = f"S = {S}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()

    # Добавляем элементы на страницу
    page.add(y_input, t_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)