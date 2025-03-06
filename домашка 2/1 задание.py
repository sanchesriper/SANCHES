import flet as ft
import numpy as np

def calculate_g(f_input, y_input, result_text):
    f = float(f_input.value)
    y = float(y_input.value)
            
    G = np.e * 2 * y + np.sin(f) / np.log10(3.8 * y + f)
            
    result_text.value = f"G = {G}"
    result_text.update()

def main(page: ft.Page):
    page.title = "Задание №1"
      
    f_input = ft.TextField(label="Введите значение для переменной f", width=200)  
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить G", on_click=lambda e: calculate_g(f_input, y_input, result_text))
    
    # Поле для отображения результата
    result_text = ft.Text(value="", size=20)

    # Добавляем элементы на страницу
    page.add(f_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)
