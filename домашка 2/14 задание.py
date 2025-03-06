import flet as ft
import numpy as np

def calculate_g(y_input, h_input, result_text):
    y = float(y_input.value)
    h = float(h_input.value)
            
    P = np.exp(y + 2.5) + 7.1 * np.power(h, 3) / np.log(np.sqrt(y + 0.04 * h * y))
            
    result_text.value = f"P = {P}"
    result_text.update()

def main(page: ft.Page):
    page.title = "Задание №13"
      
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)  
    h_input = ft.TextField(label="Введите значение для переменной h", width=200)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить P", on_click=lambda e: calculate_g(y_input, h_input, result_text))
    
    # Поле для отображения результата
    result_text = ft.Text(value="", size=20)

    # Добавляем элементы на страницу
    page.add(y_input, h_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)