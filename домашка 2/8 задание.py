import flet as ft
import numpy as np

def calculate_g(y_input, t_input, result_text):
    y = float(y_input.value)
    t = float(t_input.value)
            
    T = (2.37 * np.sin(t + 1)) / np.sqrt(4 * y**2 - 0.1 * y + 5)
            
    result_text.value = f"T = {T}"
    result_text.update()

def main(page: ft.Page):
    page.title = "Задание №8"
      
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)  
    t_input = ft.TextField(label="Введите значение для переменной t", width=200)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить T", on_click=lambda e: calculate_g(y_input, t_input, result_text))
    
    # Поле для отображения результата
    result_text = ft.Text(value="", size=20)

    # Добавляем элементы на страницу
    page.add(y_input, t_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)