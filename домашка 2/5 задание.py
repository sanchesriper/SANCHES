import flet as ft
import numpy as np

def calculate_g(f_input, y_input, a_input, result_text):
    f = float(f_input.value)
    y = float(y_input.value)
    a = float(a_input.value)
            
    D = 7.8 * a**2 + 3.52 * f / np.log(a + 2 * y) + np.exp(y)
            
    result_text.value = f"D = {D}"
    result_text.update()

def main(page: ft.Page):
    page.title = "Задание №4"
      
    f_input = ft.TextField(label="Введите значение для переменной f", width=200)  
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)
    a_input = ft.TextField(label="Введите значение для переменной a", width=200)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить D", on_click=lambda e: calculate_g(f_input, y_input, a_input, result_text))
    
    # Поле для отображения результата
    result_text = ft.Text(value="", size=20)

    # Добавляем элементы на страницу
    page.add(f_input, y_input, a_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)
