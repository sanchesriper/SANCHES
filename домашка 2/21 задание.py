import flet as ft
import numpy as np

def main(page: ft.Page):
    page.title = "Задание 21"
    
    # Создаем текстовые поля для ввода k, p, x и d
    k_input = ft.TextField(label="Введите значение для переменной k", keyboard_type=ft.KeyboardType.NUMBER)
    p_input = ft.TextField(label="Введите значение для переменной p", keyboard_type=ft.KeyboardType.NUMBER)
    x_input = ft.TextField(label="Введите значение для переменной x", keyboard_type=ft.KeyboardType.NUMBER)
    d_input = ft.TextField(label="Введите значение для переменной d", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить Q", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("Q= ", size=20)
    
    def calculate():
        try:
            k = float(k_input.value)
            p = float(p_input.value)
            x = float(x_input.value)
            d = float(d_input.value)
            
            # Проверка, чтобы избежать деления на ноль
            denominator = x - np.power(d, 3)
            if denominator == 0:
                raise ValueError("Деление на ноль! Убедитесь, что x не равно d^3.")
            
            # Вычисление Q
            Q = (np.sqrt(k) + 2.6 * p * np.sin(k)) / denominator
            result_text.value = f"Q = {Q}"
            page.update()
        except ValueError as ve:
            result_text.value = f"Ошибка: {ve}"
            page.update()
        except Exception as e:
            result_text.value = f"Ошибка: {str(e)}"
            page.update()

    # Добавляем элементы на страницу
    page.add(k_input, p_input, x_input, d_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)