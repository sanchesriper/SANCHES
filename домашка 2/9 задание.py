import flet as ft
import numpy as np

def calculate_g(y_input, w_input, result_text):
    y = float(y_input.value)
    w = float(w_input.value)
            
    V = np.power((y + 2 * w), 3) / np.log(y + 0.75)
            
    result_text.value = f"V = {V}"
    result_text.update()

def main(page: ft.Page):
    page.title = "Задание №9"
      
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)  
    w_input = ft.TextField(label="Введите значение для переменной w", width=200)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить V", on_click=lambda e: calculate_g(y_input, w_input, result_text))
    
    # Поле для отображения результата
    result_text = ft.Text(value="", size=20)

    # Добавляем элементы на страницу
    page.add(y_input, w_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)