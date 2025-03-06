import flet as ft
import numpy as np

def calculate_g(t_input, r_input, result_text):
    t = float(t_input.value)
    r = float(r_input.value)
            
    W = 4 * np.power(t, 3) + np.log(r) / (np.exp(r) + r) + 7.2 * np.sin(r)
            
    result_text.value = f"W = {W}"

def main(page: ft.Page):
    page.title = "Задание 16"
    
    # Создаем текстовые поля для ввода t и r
    t_input = ft.TextField(label="Введите значение для переменной t", keyboard_type=ft.KeyboardType.NUMBER)
    r_input = ft.TextField(label="Введите значение для переменной r", keyboard_type=ft.KeyboardType.NUMBER)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить W", on_click=lambda e: calculate())
    
    # Поле для отображения результата
    result_text = ft.Text("W= ", size=20)
    
    def calculate():
        try:
            t = float(t_input.value)
            r = float(r_input.value)
            W = 4 * np.power(t, 3) + np.log(r) / (np.exp(r) + r) + 7.2 * np.sin(r)
            result_text.value = f"W = {W}"
            page.update()
        except ValueError:
            result_text.value = "Пожалуйста, введите корректные числовые значения."
            page.update()
        except Exception as e:
            result_text.value = f"Ошибка: {str(e)}"
            page.update()

    # Добавляем элементы на страницу
    page.add(t_input, r_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)