import flet as ft
import numpy as np

def calculate_g(y_input, i_input, result_text):
    y = float(y_input.value)
    i = float(i_input.value)
            
    L = (0.81 * np.cos(i)) / np.log(y) + 2 * (i ** 3)
            
    result_text.value = f"L = {L}"
    result_text.update()

def main(page: ft.Page):
    page.title = "Задание №6"
      
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)  
    i_input = ft.TextField(label="Введите значение для переменной i", width=200)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить L", on_click=lambda e: calculate_g(y_input, i_input, result_text))
    
    # Поле для отображения результата
    result_text = ft.Text(value="", size=20)

    # Добавляем элементы на страницу
    page.add(y_input, i_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)
