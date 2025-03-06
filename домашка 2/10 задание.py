import flet as ft
import numpy as np

def calculate_g(t_input, y_input, result_text):
    t = float(t_input.value)
    y = float(y_input.value)
            
    R = (2 * t + y * np.cos(t)) / np.sqrt(y + 4.831)
            
    result_text.value = f"R = {R}"
    result_text.update()

def main(page: ft.Page):
    page.title = "Задание №10"
      
    t_input = ft.TextField(label="Введите значение для переменной t", width=200)  
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить R", on_click=lambda e: calculate_g(t_input, y_input, result_text))
    
    # Поле для отображения результата
    result_text = ft.Text(value="", size=20)

    # Добавляем элементы на страницу
    page.add(t_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)
