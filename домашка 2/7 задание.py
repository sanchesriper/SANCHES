import flet as ft
import numpy as np

def calculate_g(y_input, m_input, result_text):
    y = float(y_input.value)
    m = float(m_input.value)
            
    N = (m**2 + 2.8 * m + 0.355) / (np.cos(2 * y) + 3.6)
            
    result_text.value = f"N = {N}"
    result_text.update()

def main(page: ft.Page):
    page.title = "Задание №7"
      
    y_input = ft.TextField(label="Введите значение для переменной y", width=200)  
    m_input = ft.TextField(label="Введите значение для переменной m", width=200)

    # Создаем кнопку для вычисления
    calculate_button = ft.ElevatedButton(text="Вычислить N", on_click=lambda e: calculate_g(y_input, m_input, result_text))
    
    # Поле для отображения результата
    result_text = ft.Text(value="", size=20)

    # Добавляем элементы на страницу
    page.add(y_input, m_input, calculate_button, result_text)

# Запускаем приложение
ft.app(target=main)