import flet as ft
import numpy as np

def calculate_g(k_input, y_input, result_text):
    k = float(k_input.value)
    y = float(y_input.value)
            
    U = np.log(k - y) + (y ** 4) / (np.exp(y)) + 2.355 * (k ** 2)
            
    result_text.value = f"U = {U}"
    result_text.update()

def main(page: ft.Page):
    page.title = "Задание №3"
      
    k_input = ft.TextField(label="Введите значение для переменной k", width=200)  
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить U", on_click=lambda e: calculate_g(k_input, y_input, result_text))
    
    # Поле для отображения результата
    result_text = ft.Text(value="", size=20)

    # Добавляем элементы на страницу
    page.add(k_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)
