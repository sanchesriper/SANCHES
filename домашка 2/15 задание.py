import flet as ft
import numpy as np

def calculate_g(y_input, j_input, result_text):
    y = float(y_input.value)
    j = float(j_input.value)
            
    F = 2 * np.sin(0.354 * y + 1) / np.log(y + 2 * j) * y
            
    result_text.value = f"F = {F}"
    result_text.update()

def main(page: ft.Page):
    page.title = "Задание №15"
      
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)  
    j_input = ft.TextField(label="Введите значение для переменной j", width=200)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить F", on_click=lambda e: calculate_g(y_input, j_input, result_text))
    
    # Поле для отображения результата
    result_text = ft.Text(value="", size=20)

    # Добавляем элементы на страницу
    page.add(y_input, j_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)