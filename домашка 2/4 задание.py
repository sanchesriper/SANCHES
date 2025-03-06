import flet as ft
import numpy as np

def calculate_g(f_input, w_input, y_input, result_text):
    f = float(f_input.value)
    w = float(w_input.value)
    y = float(y_input.value)
            
    G = 9.33 * w**3 + (np.sqrt(w) / np.log(y + 3.5)) + np.sqrt(y)
            
    result_text.value = f"G = {G}"
    result_text.update()

def main(page: ft.Page):
    page.title = "Задание №4"
      
    f_input = ft.TextField(label="Введите значение для переменной f", width=200)  
    w_input = ft.TextField(label="Введите значение для переменной w", width=200)
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить G", on_click=lambda e: calculate_g(f_input, w_input, y_input, result_text))
    
    # Поле для отображения результата
    result_text = ft.Text(value="", size=20)

    # Добавляем элементы на страницу
    page.add(f_input, w_input, y_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)
