import flet as ft
import numpy as np

def calculate_g(y_input, n_input, result_text):
    y = float(y_input.value)
    n = float(n_input.value)
            
    D = np.power(y, 2) + 0.5 * n + 4.8 / np.sin(y)
            
    result_text.value = f"D = {D}"
    result_text.update()

def main(page: ft.Page):
    page.title = "Задание №11"
      
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)  
    n_input = ft.TextField(label="Введите значение для переменной n", width=200)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить D", on_click=lambda e: calculate_g(y_input, n_input, result_text))
    
    # Поле для отображения результата
    result_text = ft.Text(value="", size=20)

    # Добавляем элементы на страницу
    page.add(y_input, n_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)